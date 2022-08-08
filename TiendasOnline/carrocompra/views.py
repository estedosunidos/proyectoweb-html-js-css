from django.shortcuts import render,redirect
from .carrocompra import carrocompra
from Tienda.models import Producto
# Create your views here.
def agregar_producto(request,producto_id):
    carrocompras=carrocompra(request)
    producto=Producto.objects.get(id=producto_id)
    carrocompras.agregar_producto(producto=producto)
    return redirect("Tienda")
def eliminar_producto(request,producto_id):
    carrocompra=carrocompra(request)
    producto=Producto.objects.get(id=producto_id)
    carrocompra.eliminar_producto(producto=producto)
    return redirect("Tienda")
def resta_producto(request,producto_id):
    carrocompra=carrocompra(request)
    producto=Producto.objects.get(id=producto_id)
    carrocompra.resta_producto(producto=producto)
    return redirect("Tienda")
def limpiar(request,producto_id):
    carrocompra=carrocompra(request)
    carrocompra.limpiar()
    return redirect("Tienda")