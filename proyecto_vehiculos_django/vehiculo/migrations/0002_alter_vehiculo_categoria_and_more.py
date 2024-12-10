# Generated by Django 4.2.16 on 2024-11-08 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('particular', 'Particular'), ('transporte', 'Transporte'), ('carga', 'Carga')], default='particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 14, 54, 38, 723849)),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_modificacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 14, 54, 38, 723849)),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('fiat', 'Fiat'), ('chevrolet', 'Chevrolet'), ('ford', 'Ford'), ('toyota', 'Toyota')], default='ford', max_length=20),
        ),
    ]
