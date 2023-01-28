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
    return redirect('horarios')

def indexUc(request):
    lista_ucs = Uc.objects.all()
                
    return render (request, 'asistencia/index_ucs.html', {'lista_ucs': lista_ucs})

def indexDocente(request):
    lista_docentes = Docente.objects.all()
                
    return render (request, 'asistencia/index_docentes.html', {'lista_docentes': lista_docentes})

def indexHorario(request):
    lista_horarios = Horario.objects.all().order_by('dia',)
                
    return render (request, 'asistencia/index_horarios.html', {'lista_horarios': lista_horarios})

def crearUc(request):
    form = FormUc()
    if request.method == 'POST':
        form = FormUc(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ucs')
            
    return render (request, 'asistencia/form_uc.html', {'form': form})

def crearDocente(request):
    form = FormDocente()
    if request.method == 'POST':
        form = FormDocente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docentes')
            
    return render (request, 'asistencia/form_docente.html', {'form': form})

def crearHorario(request):
    form = FormHorario()
    if request.method == 'POST':
        form = FormHorario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horarios')
            
    return render (request, 'asistencia/form_horario.html', {'form': form})