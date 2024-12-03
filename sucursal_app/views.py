from django.shortcuts import render,redirect

# Create your views here.
from .models import Sucursales

# Create your views here.

def inicio_vistaSucursales(request):
    su = Sucursales.objects.all()
    return render(request, 'gestionarSucursales.html', {'Su': su})

def registrarSucursales(request):
    Id_Sucursal =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    direccion = request.POST['txtdireccion']
    horario = request.POST['txthorario']
    telefono = request.POST['txttelefono']
    email = request.POST['txtemail']
    ciudad = request.POST['txtciudad']
    
    guardarSu = Sucursales.objects.create(Id_Sucursal=Id_Sucursal, nombre=nombre, direccion=direccion,
                                                    horario=horario, telefono=telefono, email=email, ciudad=ciudad)
    return redirect('sucursales')

def seleccionarSucursales( request, Id_Sucursal):
    Sucursales_ = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    return render(request, 'editarSucursales.html', {'Su': Sucursales_})

def editarSucursales(request):
    Id_Sucursal =  request.POST['txtid']
    nombre =  request.POST['txtnombre'] 
    direccion = request.POST['txtdireccion']
    horario = request.POST['txthorario']
    telefono = request.POST['txttelefono']
    email = request.POST['txtemail']
    ciudad = request.POST['txtciudad']
    
    Sucursales_ = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    Sucursales_.nombre = nombre
    Sucursales_.direccion=direccion
    Sucursales_.horario=horario
    Sucursales_.telefono=telefono
    Sucursales_.email=email
    Sucursales_.ciudad=ciudad
    Sucursales_.save()
    return redirect('sucursales')

def borrarSucursales(request,Id_Sucursal):
    Sucursales_=Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    Sucursales_.delete()
    return redirect("sucursales")