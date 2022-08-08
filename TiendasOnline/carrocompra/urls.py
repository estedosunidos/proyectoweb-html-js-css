from tokenize import Name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="carro"
urlpatterns = [
    path("agregar/<int:producto_id>/",views.agregar_producto,name="agregar"),
    path("eliminar/<int:producto_id>/",views.eliminar_producto,name="eliminar"),
    path("restar/<int:producto_id>/",views.resta_producto,name="restae"),
    path("limpiar/",views.limpiar,name="limpiar"),
    
]
