from django.urls import path
from . import views
# importar views
from .views import IndexPageView, lista_vehiculos,crear_vehiculo, editar_vehiculo, eliminar_vehiculo, registro, iniciar_sesion, home_page, cerrar_sesion

urlpatterns = [
    #path ( ruta, view, name=nombre_de_la_ruta)
    path('', IndexPageView.as_view(), name="index"),
    path('lista_vehiculos/', lista_vehiculos, name='lista_vehiculos'),
    path('crear_vehiculo/', crear_vehiculo, name='crear_vehiculo'), # registrando ruta para crear vehiculo
    path('editar_vehiculo/<int:vehiculo_id>', editar_vehiculo, name='editar_vehiculo'), # registrando ruta para editar vehiculo
    path('eliminar_vehiculo/<int:vehiculo_id>', eliminar_vehiculo, name='eliminar_vehiculo'), # registrando ruta para eliminar vehiculo
    path('registro/', registro, name='registro'),   #registra ruta de formulario de registro
    path('login/', iniciar_sesion ,name='login'),   #registra rura para el login
    path('home/', home_page, name='home'),           #registra ruta para la pagina principal del usuario logeado
    path('logout/', cerrar_sesion, name='logout')
]