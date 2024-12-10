from django import forms
from .models import Vehiculo

# https://docs.djangoproject.com/en/5.1/topics/forms/
# https://docs.djangoproject.com/en/5.1/ref/forms/widgets/
class VehiculoForm(forms.ModelForm):
    
    class Meta: # clase meta para definir caracteristicas del objeto
        model = Vehiculo # modelo a utilizar
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor','categoria','precio']
        widgets = {
            'marca' : forms.Select(
                attrs={
                    'class': 'form-control', 
                    'placeholder':'Ingrese marca del vehiculo',
                    'required': True
                }),
            'modelo' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el modelo del vehiculo',
                    'required': True
                }),
            'serial_carroceria' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la serial_carroceria del vehiculo',
                    'required': True
                }),
            'serial_motor' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la serial_carroceria del vehiculo',
                    'required': True
                }),
            'categoria' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la categoria del vehiculo',
                    'required': True
                }),
            'precio' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el precio del vehiculo',
                    'required': True
                })
        }
