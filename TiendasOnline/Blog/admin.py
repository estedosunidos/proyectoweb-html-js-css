from django.contrib import admin
from .models import Categoria,Post
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin): 
    readonly_fields = ('create', 'update')
admin.site.register(Categoria,CategoriaAdmin)
class PostAdmin(admin.ModelAdmin): 
    readonly_fields = ('create', 'update')
admin.site.register(Post,PostAdmin)