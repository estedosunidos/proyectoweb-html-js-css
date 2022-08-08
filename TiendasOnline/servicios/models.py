from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models

# Create your models here.
class Servicios(models.Model):
    titulo=models.CharField(max_length=255, blank=True)
    contenido=models.CharField(max_length=255, blank=True)
    imagen=models.ImageField(upload_to='servicios')
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        def __str__(self):
            return self.titulo
        
