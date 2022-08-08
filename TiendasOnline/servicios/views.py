from django.shortcuts import render
from servicios.models import  Servicios
# Create your views here.
def servicio(request):
    servicios=Servicios.objects.all()
    return render(request, 'servicios/service.html',{"servicios":servicios})