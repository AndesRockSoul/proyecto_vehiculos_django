import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo   # Asegúrate de que Book esté correctamente importado
from .forms import VehiculoForm




# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'index.html'

@login_required  #se carga el decorator, para que se pueda acceder solo si esta logeado a la funcion
#@permission_required('vehiculo.view')
def lista_vehiculos(request):
    # Inicializar el formulario de filtros
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})




# https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/
# https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
@login_required
@permission_required('vehiculo.can_add_vehiculo_model')  #@permission_required('vehiculo.can_add_vehiculo_model', raise_exception=True)  manda a pagina 404 forbidden, si no redirige al inicio
def crear_vehiculo(request):
    if request.method == 'POST': # si el metodo es POST
        form = VehiculoForm(request.POST)
        if form.is_valid(): # si el formulario es validofrom django.contrib import messages
            form.save() # guarda los datos en la base de datos
            messages.success(request, 'Vehiculo creado correctamente') # muestra un mensaje https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            return redirect('lista_vehiculos') # redirecciona a lista_libros
        else: # si el formulario no es valido
            messages.error(request, 'Modifica los datos de ingreso, no se ha podido crear') # muestra un mensaje
            return HttpResponseRedirect(reverse('crear_vehiculo')) # redirecciona a la pagina
    else: # si el metodo es GET
        form = VehiculoForm()
        return render(request, 'crear_vehiculo.html', {'form': form})
    
@login_required    
@permission_required('vehiculo.can_add_vehiculo_model') 
def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk = vehiculo_id) # obteniendo el vehiculo a editar en la db o status 404 not found
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo) # instancia del formulario con los datos del vehiculo a editar
        if form.is_valid(): # si el formulario es valido
            vehiculo = form.save() # guarda los datos en la base de datos #vehiculo = form.save(commit=False) 
            vehiculo.fecha_modificacion = datetime.datetime.now()   #guarda la fecha de modificacion
            vehiculo.save()   #guarda los datos rn la base de datos
            messages.success(request,'vehiculo editado correctamente')
            return redirect('lista_vehiculos') # redirecciona a lista de libros
        else:  # si el formulario no es valido
            messages.error(request, 'Modifique los datos de ingreso, no se ha podido editar') # muestra un mensaje
            return HttpResponseRedirect(reverse('editar_vehiculo', args=[vehiculo.id])) # redirecciona a la pagina
    else: # si el metodo es GET
        form = VehiculoForm(instance=vehiculo) # instancia del formulario con los datos del vehiculo a editar
        return render(request, 'editar_vehiculo.html', {'form': form, 'vehiculo_id': vehiculo_id}) # renderiza la vista para editar el vehiculo
    
@login_required
@permission_required('vehiculo.can_add_vehiculo_model') 
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id) # obteniendo el vehiculo a eliminar en la db o status 404 not found
    #agregar una alerta con aceptar y cancel, acepat sigue la fincion cancela, hace exit inmediato de la funcion sin retornar la eliminiacion, 
    #e indicar quizas el libro que se esta eliminando llamando el id
    vehiculo.delete() # eliminando el libro de la base de datos
    messages.info(request, 'Vehiculo eliminado correctamente') # muestra un mensaje
    return redirect('lista_vehiculos')  # redirecciona a lista de libros



def registro(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardando el usuario en una variable sin guardar en la base de datos
            
            # Obtener el tipo de contenido y el permiso
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permission = Permission.objects.get(
                codename='development',
                content_type=content_type,
            )
            
            # Añadir el permiso al usuario
            user.user_permissions.add(permission)
            
            # Guardar el usuario en la base de datos después de asignar los permisos
            user.save()
            
            messages.success(request, 'Registro éxitoso')
            return redirect('login')
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:   # si se recibieron datos en user (si existe el usuario) luego del authenticate
            login(request, user)  #se persiste la sesion del usuario con esa data del usuario
            return redirect('lista_vehiculos')   #si usuario ingresa se va a la pagina indicada
        else:
            messages.error(request, 'No te has podido logear. Credenciales inválidas!')
            return render(request, 'login.html')  
    else: #cuando es una peticion de tipo get(u otra) se retorna a la pagina de login para la revalidacion
        return render(request, 'login.html')


def home_page(request):
    return render(request, 'index.html')

@login_required
def cerrar_sesion(request):
    logout(request)   #cierra a sesion del usuario logeado
    return render(request, 'index.html')

