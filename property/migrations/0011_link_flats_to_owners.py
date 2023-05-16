# Generated by Django 3.2 on 2023-05-10 05:28

from django.db import migrations


def link_flats_to_owners(apps, schema_editor):
    """Make links between flats and owners tables"""
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for owner in Owner.objects.all().iterator():
        print(f'Make links with Owner - {owner.name}')
        flats_by_owner = Flat.objects.filter(owner=owner.name)
        owner.flats.set(flats_by_owner)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner_copy_from_flat'),
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners),
    ]
