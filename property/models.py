from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    """Flat model class"""
    owner = models.CharField('ФИО владельца', max_length=200)
    
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца', null=True, blank=True)
    
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', default=None, db_index=True)
    
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField('Новостройка', default=None, null=True, blank=True)
 
    liked_by = models.ManyToManyField('UserProfile', verbose_name='кто лайкнул', related_name='liked_flats', blank=True)


    def __str__(self):
        """Object string representation"""
        return f'{self.town}, {self.address} ({self.price}р.)'


class UserProfile(models.Model):
    """User wrapping class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Object string representation"""
        return f'{self.user}'


class Owner(models.Model):
    """Flat owner data model"""
    owner_name = models.CharField('ФИО владельца', max_length=100)

    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца', null=True, blank=True)

    flats = models.ManyToManyField('Flat', verbose_name='Квартиры в собственности', related_name='owners')

    def __str__(self):
       """Object string representation"""
       return f'{self.owner_name}'
    

class Complaint(models.Model):
    """Complaint model class"""
    user = models.ForeignKey(UserProfile, verbose_name='Кто жаловался', on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, verbose_name='Квартира, на которую жаловались', on_delete=models.CASCADE)
    text = models.TextField('Текст жалобы', null=True)
