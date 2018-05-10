# from django.http import HttpResponse (Funciona para poner html limpio en la paguina pasandolo como argumento)
from django.shortcuts import render

def home (request):
    return render (request, 'core/home.html')

def about (request):
    return render (request, 'core/about.html')


def contact (request):
    return render (request, 'core/contact.html')
