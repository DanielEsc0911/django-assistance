from django import template 
from django.conf import settings
from django.urls import reverse, path, re_path
from django.template import loader
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Create your views here.

def indexHome(request):
    return redirect('crear_docente')

def indexDocente(request):
    lista_docentes = Docente.objects.all()
                
    return render (request, 'asistencia/index_docentes.html', {'lista_docentes': lista_docentes})

def crearDocente(request):
    form = FormDocente()
    if request.method == 'POST':
        form = FormDocente(request.POST)
        if form.is_valid():
            form.save()
            
    return render (request, 'asistencia/form_docente.html', {'form': form})