from django.shortcuts import render,redirect

# Create your views here.
from .models import Producto

# Create your views here.

def inicio_vistaProductos(request):
    losproductos = Producto.objects.all()

    return render(request,"gestionarProductos.html",{"misproductos":losproductos})



def registrarProductos(request):
    id_producto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombreproducto"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    tipo_producto = request.POST["txttipoproducto"]
    lote = request.POST["txtlote"]
    marca = request.POST["txtmarca"]


    guardarproducto = Producto.objects.create(id_producto=id_producto, nombre=nombre, descripcion=descripcion,
                                            precio=precio, tipo_producto=tipo_producto, lote=lote, marca=marca )

    return redirect("productos")

def seleccionarProductos(request, id_producto):
    clientes = Producto.objects.get(id_producto = id_producto)

    return render(request,"editarProductos.html",{"misproductos":clientes})


def editarProductos(request):
    id_producto = request.POST["txtidproducto"]
    nombre = request.POST["txtnombreproducto"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    tipo_producto = request.POST["txttipoproducto"]
    lote = request.POST["txtlote"]
    marca = request.POST["txtmarca"]


    productos = Producto.objects.get(id_producto = id_producto)
    productos.nombre = nombre
    productos.descripcion = descripcion
    productos.precio = precio
    productos.tipo_producto = tipo_producto
    productos.lote = lote
    productos.marca = marca
    
    productos.save()

    return redirect("productos")


def borrarProductos(request, id_producto):
    productos = Producto.objects.get(id_producto = id_producto)
    productos.delete()

    return redirect("productos")