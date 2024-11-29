from django.shortcuts import render,redirect
from .models import Empleado

# Create your views here.

def inicio_vistaEmpleados(request):
    losclientes = Empleado.objects.all()

    return render(request,"gestionarEmpleado.html",{"misempleados":losclientes})



def registrarEmpleado(request):
    id_empleado = request.POST["txtidempleado"]
    nombre = request.POST["txtnombreempleado"]
    apellidos = request.POST["txtapellidos"]
    puesto = request.POST["txtpuesto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]

    guardarcliente = Empleado.objects.create(id_empleado=id_empleado, nombre=nombre, apellidos=apellidos,
                                            puesto=puesto, telefono=telefono, direccion=direccion, email=email)

    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleados = Empleado.objects.get(id_empleado = id_empleado)

    return render(request,"editarEmpleado.html",{"misempleados":empleados})


def editarEmpleado(request):
    id_empleado = request.POST["txtidempleado"]
    nombre = request.POST["txtnombreempleado"]
    apellidos = request.POST["txtapellido"]
    puesto = request.POST["txtpuesto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]

    empleado = Empleado.objects.get(id_empleado = id_empleado)
    empleado.nombre = nombre
    empleado.apellidos = apellidos
    empleado.puesto = puesto
    empleado.telefono = telefono
    empleado.email = email
    empleado.direccion = direccion

    empleado.save()

    return redirect("empleados")


def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado = id_empleado)
    empleado.delete()

    return redirect("empleados")