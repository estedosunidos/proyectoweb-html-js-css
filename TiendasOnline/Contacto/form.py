from email.headerregistry import ContentDispositionHeader
from django import forms
class Formulario(forms.Form):
    Nombre=forms.CharField(label="Nombre",required=True)
    Email=forms.CharField(label="Email", required=True)
    Contenido=forms.CharField(label="Contenido", required=True,widget=forms.Textarea)
    