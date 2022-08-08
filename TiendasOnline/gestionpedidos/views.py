from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    return render(request, 'home.html')


