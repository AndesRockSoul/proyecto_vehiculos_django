from django.contrib import admin
from .models import Vehiculo
      
# Register your models here.
#clase que hereda del model.admin
class  VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo','serial_carroceria', 'serial_motor','categoria', 'precio', 'condicion_de_precio')
    list_filter = ('precio', 'marca','categoria')
    
    def condicion_de_precio(self,obj):
        if obj.precio <= 10000 :
            return 'baja'
        elif 10000 < obj.precio < 30000:
            return 'media'
        else:
            return 'alta'

admin.site.register(Vehiculo, VehiculoAdmin)   #registro de los model separados por coma


