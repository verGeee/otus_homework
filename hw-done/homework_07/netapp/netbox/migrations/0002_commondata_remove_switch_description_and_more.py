# Generated by Django 4.0.5 on 2022-07-03 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufactured', models.CharField(max_length=15)),
                ('model_name', models.CharField(max_length=20)),
                ('sn', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='switch',
            name='description',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='id',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='manufactured',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='sn',
        ),
        migrations.AddField(
            model_name='switch',
            name='port_count',
            field=models.IntegerField(default='0'),
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='netbox.commondata')),
                ('prefix_count', models.IntegerField(default='0')),
            ],
            bases=('netbox.commondata',),
        ),
        migrations.AddField(
            model_name='switch',
            name='commondata_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='netbox.commondata'),
            preserve_default=False,
        ),
    ]
