from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    """Flat model class"""

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

    has_balcony = models.BooleanField('Наличие балкона',
                                      default=None,
                                      db_index=True)

    active = models.BooleanField('Активно-ли объявление', db_index=True)

    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField('Новостройка', default=None,
                                       null=True, blank=True)

    liked_by = models.ManyToManyField(User,
                                      verbose_name='кто лайкнул',
                                      related_name='liked_flats',
                                      blank=True)

    def __str__(self):
        """Object string representation"""
        return f'{self.town}, {self.address}'


class Owner(models.Model):
    """Flat owner data model"""

    name = models.CharField('ФИО владельца',
                            max_length=100,
                            db_index=True)

    phone_number = models.CharField('Номер владельца',
                                    max_length=20,
                                    db_index=True)

    pure_phone_number = PhoneNumberField('Нормализованный номер владельца',
                                         null=True,
                                         blank=True,
                                         db_index=True)

    flats = models.ManyToManyField('Flat',
                                   verbose_name='Квартиры в собственности',
                                   related_name='owners')

    def __str__(self):
        """Object string representation"""
        return self.name


class Complaint(models.Model):
    """Complaint model class"""

    user = models.ForeignKey(User,
                             verbose_name='Кто жаловался',
                             on_delete=models.DO_NOTHING,
                             related_name='complaints')

    flat = models.ForeignKey(Flat,
                             verbose_name='Квартира, на которую жаловались',
                             on_delete=models.CASCADE,
                             related_name='complaints')

    text = models.TextField('Текст жалобы', null=True)

    def __str__(self):
        """Object string representation"""
        return f'Flat - {self.flat}, person - {self.user}'
