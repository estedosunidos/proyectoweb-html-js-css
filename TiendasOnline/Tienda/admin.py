from django.contrib import admin
from .models import Categoria,Producto
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin): 
    readonly_fields = ('create', 'update')
admin.site.register(Categoria,CategoriaAdmin)
class productoadmin(admin.ModelAdmin): 
    readonly_fields = ('create', 'update')

admin.site.register(Producto,productoadmin)