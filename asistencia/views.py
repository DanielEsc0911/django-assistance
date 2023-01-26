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
    return redirect('docentes')

def indexRegistro(request):
    lista_registros = Registro.objects.all()
                
    return render (request, 'asistencia/index_registros.html', {'lista_registros': lista_registros})

def addEntrada(request, pk):
    item = Registro.objects.get(pk=pk)
    item.entrada = timezone.now()
    item.save()
    return redirect('registros')

def addSalida(request, pk):
    item = Registro.objects.get(pk=pk)
    item.salida = timezone.now()
    item.save()
    return redirect('registros')

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