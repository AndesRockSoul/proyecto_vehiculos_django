# Generated by Django 5.1.2 on 2024-11-08 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
                ('precio', models.IntegerField(help_text='Condición precio entre 0 y 30000')),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime(2024, 11, 8, 0, 38, 13, 287207))),
                ('fecha_modificacion', models.DateTimeField(default=datetime.datetime(2024, 11, 8, 0, 38, 13, 287207))),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'permissions': [('vehiculo.view', 'Puede ver los vehiculos'), ('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')],
            },
        ),
    ]
