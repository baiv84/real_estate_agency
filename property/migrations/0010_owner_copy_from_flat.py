from django.db import migrations


def copy_flat_owners(apps, schema_editor):
    """Copy flat owners to Owner table"""
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner_name = flat.owner
        owners_phonenumber = flat.owners_phonenumber
        owner_pure_phone =  flat.owner_pure_phone
        owner, created = Owner.objects.get_or_create(name=owner_name,
                                                     phone_number=owners_phonenumber,
                                                     pure_phone_number=owner_pure_phone
                                                    )
        if created:
            print(f'Created new owner - {owner}')


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_make_indexes'),
    ]

    operations = [
         migrations.RunPython(copy_flat_owners),
    ]
