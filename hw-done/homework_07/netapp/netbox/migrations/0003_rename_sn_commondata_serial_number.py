# Generated by Django 4.0.5 on 2022-07-03 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox', '0002_commondata_remove_switch_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commondata',
            old_name='sn',
            new_name='serial_number',
        ),
    ]