# Generated by Django 4.0.5 on 2022-07-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox', '0009_alter_commondata_manufactured'),
    ]

    operations = [
        migrations.AddField(
            model_name='commondata',
            name='name',
            field=models.CharField(default='-', max_length=10),
        ),
    ]
