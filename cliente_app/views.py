from django.shortcuts import render,redirect
from .models import Clientes

# Create your views here.

def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all()

    return render(request,"gestionarCliente.html",{"misclientes":losclientes})



def registrarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombrecliente"]
    apellidoP = request.POST["txtapellidoP"]
    apellidoM = request.POST["txtapellidoM"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]

    guardarcliente = Clientes.objects.create(id_cliente=id_cliente, nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM,
                                            direccion=direccion, telefono=telefono)

    return redirect("clientes")

def seleccionarCliente(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente = id_cliente)

    return render(request,"editarCliente.html",{"misclientes":clientes})


def editarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombrecliente"]
    apellidoP = request.POST["txtapellidoP"]
    apellidoM = request.POST["txtapellidoM"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]

    cliente = Clientes.objects.get(id_cliente = id_cliente)
    cliente.nombre = nombre
    cliente.apellidoP = apellidoP
    cliente.apellidoM = apellidoM
    cliente.direccion = direccion
    cliente.telefono = telefono
    
    cliente.save()

    return redirect("clientes")


def borrarCliente(request , id_cliente):
    clientes = Clientes.objects.get(id_cliente = id_cliente)
    clientes.delete()

    return redirect("clientes")