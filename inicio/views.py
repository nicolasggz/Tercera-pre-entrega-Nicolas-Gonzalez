from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')


def crear_gato(request):
    return render(request, 'inicio/crear_gato.html')