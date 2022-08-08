from django.db import models
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
class Post(models.Model):
    titulo=models.CharField(max_length=255, blank=True)
    contenido=models.CharField(max_length=255, blank=True)
    imagen=models.ImageField(upload_to='Blog',null=True, blank=True)
    categoria=models.ManyToManyField(Categoria)
    autor=models.ForeignKey(User, blank=True, null  = True,on_delete=models.CASCADE)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        def __str__(self):
            return self.titulo
        