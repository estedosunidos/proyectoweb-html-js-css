from math import prod
from django.shortcuts import render
from .models import Producto

# Create your views here.
def tienda(request):
    producto=Producto.objects.all()
    return render(request, 'Tienda/tienda.html',{"producto":producto})