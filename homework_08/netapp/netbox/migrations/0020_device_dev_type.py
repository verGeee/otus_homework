# Generated by Django 4.0.5 on 2022-07-12 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netbox', '0019_devicetype_remove_device_dev_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='dev_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='netbox.devicetype'),
            preserve_default=False,
        ),
    ]
