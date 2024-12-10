from django.db import models
import datetime


# Create your models here.
# https://docs.djangoproject.com/en/5.1/topics/db/models/
# https://www.w3schools.com/django/django_models.php
class Vehiculo(models.Model):
    
    #tipos de categorias
    MARCAS = [('Fiat','Fiat'),
              ('Chevrolet','Chevrolet'),
              ('Ford','Ford'),
              ('Toyota','Toyota'),
              ]
    
    CATEGORIAS = [('Particular','Particular'),
                  ('Transporte','Transporte'),
                  ('Carga','Carga'),       
                  ]
    
    # atributos
    marca = models.CharField(max_length = 20, null = False, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length = 100, null = False)
    serial_carroceria = models.CharField(max_length = 50, null = False)
    serial_motor = models.CharField(max_length = 50, null = False)
    categoria = models.CharField(max_length = 20, null = False, choices=CATEGORIAS, default='Particular')
    precio = models.IntegerField(help_text = 'Condición precio entre 0 y 30000')
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now())
    
    def condicion_de_precio(self): 
        if self.precio <= 10000 :
            return 'baja'
        elif 10000 < self.precio < 30000:
            return 'media'
        else:
            return 'alta'
    
        
    class Meta:
        verbose_name = 'Vehiculo'           #se modificó el modelo Book para que en el sitio admin se lea con este nick
        verbose_name_plural = 'Vehiculos'
            
        permissions = [
                # ('permiso', 'descripcion') 
                # https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#custom-permissions
                ('vehiculo.view', 'Puede ver los vehiculos'),
                ('visualizar_catalogo','Puede ver lista de vehiculos'), #se le asigna automaticamente al registrarse
                ('can_add_vehiculo_model', 'Can add vehiculo model'),    #puede agregar los vehiculos  en el interfaz y en el administrador
                ('development', 'Permiso como Desarrollador'),
                ('scrum_master', 'Permiso como Scrum Master'),
                ('product_owner', 'Permiso como Product Owner')
            ]