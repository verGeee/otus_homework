# Generated by Django 4.0.5 on 2022-07-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox', '0008_alter_commondata_manufactured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commondata',
            name='manufactured',
            field=models.CharField(choices=[('Arista', 'Arista'), ('Cisco', 'Cisco'), ('Mellanox', 'Mellanox'), ('Juniper', 'Juniper')], max_length=20),
        ),
    ]
