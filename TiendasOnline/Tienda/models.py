from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=255, blank=True)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        def __str__(self):
            return self.nombre
class Producto(models.Model):
    nombre=models.CharField(max_length=255, blank=True)
    precio=models.FloatField(null=True, blank=True)
    imagen=models.ImageField(upload_to='Tienda',null=True, blank=True)
    categorias=models.ForeignKey(Categoria, blank=True, null  = True,on_delete=models.CASCADE)
    disponibilidad=models.BooleanField(default=True)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        def __str__(self):
            return self.nombre
        def __str__(self):
            return self.categorias
        