# Generated by Django 4.2.16 on 2024-11-08 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_vehiculo_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 15, 14, 20, 331534)),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_modificacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 15, 14, 20, 331534)),
        ),
    ]
