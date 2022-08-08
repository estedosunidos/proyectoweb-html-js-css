from django.shortcuts import redirect, render
from .form import Formulario
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    formulario_contacto=Formulario()
    if request.method == 'POST':
        formulario_contacto=Formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('Nombre')
            email=request.POST.get('Email')
            contenido=request.POST.get('Contenido')
            email=EmailMessage("Mensaje desde app django","El usuario con nombre {} con la direccion {} escribe lo siguente{}".format(nombre,email,contenido),"",["ivanestebanvargasmartines@gmail.com"],reply_to=[email])    
            try:
                email.send()
                return redirect("/Contacto/?valido")
            except:
                return redirect("/Contacto/?novalido")
    return render(request, 'Contactos/contacto.html',{"miformulario":formulario_contacto})