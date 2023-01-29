from django import template 
from django.conf import settings
from django.urls import reverse, path, re_path
from django.template import loader
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *

# Create your views here.

def Redir(request):
    return redirect('home')

@login_required(login_url='/login/')
def indexHome(request):
    lista_ucs = Uc.objects.all().reverse().reverse()[:3]
    lista_docentes = Docente.objects.all().reverse().reverse()[:3]
    lista_horarios = Horario.objects.all().order_by('dia', 'uc', 'seccion')

    context = {
        'lista_ucs': lista_ucs,
        'lista_docentes': lista_docentes,
        'lista_horarios': lista_horarios,
    }

    return render (request, 'asistencia/home.html', context)

@login_required(login_url='/login/')
def indexUc(request):
    lista_ucs = Uc.objects.all()
                
    return render (request, 'asistencia/index_ucs.html', {'lista_ucs': lista_ucs})

@login_required(login_url='/login/')
def indexDocente(request):
    lista_docentes = Docente.objects.all()
                
    return render (request, 'asistencia/index_docentes.html', {'lista_docentes': lista_docentes})

@login_required(login_url='/login/')
def indexHorario(request):
    lista_horarios = Horario.objects.all().order_by('dia', 'uc', 'seccion')
                
    return render (request, 'asistencia/index_horarios.html', {'lista_horarios': lista_horarios})

@login_required(login_url='/login/')
def indexAsistencia(request):
    lista_asistencias = Asistencia.objects.all().order_by('fecha',)
                
    return render (request, 'asistencia/index_asistencia.html', {'lista_asistencias': lista_asistencias})

@login_required(login_url='/login/')
def indexAsistenciaDocente(request, pk):
    lista_asistencias = Asistencia.objects.filter(docente__pk=pk).order_by('fecha',)
                
    return render (request, 'asistencia/index_asistencia.html', {'lista_asistencias': lista_asistencias})

#--------------------------------------------------------------CRUD

#--------------------------------------------------------------Create
@login_required(login_url='/login/')
@permission_required('asistencia.add_uc', raise_exception=True)
def crearUc(request):
    form = FormUc()
    if request.method == 'POST':
        form = FormUc(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ucs')     
    return render (request, 'asistencia/form_uc.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('asistencia.add_docente', raise_exception=True)
def crearDocente(request):
    form = FormDocente()
    if request.method == 'POST':
        form = FormDocente(request.POST)
        if form.is_valid():
            cap = form.save(commit=False)
            cap.nombre = cap.nombre.capitalize()
            cap.apellido = cap.apellido.capitalize()
            cap.save()
            return redirect('docentes')
            
    return render (request, 'asistencia/form_docente.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('asistencia.add_horario', raise_exception=True)
def crearHorario(request):
    form = FormHorario()
    if request.method == 'POST':
        form = FormHorario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horarios')
            
    return render (request, 'asistencia/form_horario.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('asistencia.add_horario', raise_exception=True)
def crearAsistencia(request):
    form = FormAsistencia()
    if request.method == 'POST':
        form = FormAsistencia(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencias')
            
    return render (request, 'asistencia/form_asistencia.html', {'form': form})
#--------------------------------------------------------------


#--------------------------------------------------------------Update
@login_required(login_url='/login/')
@permission_required('asistencia.change_uc', raise_exception=True)
def editUc(request, pk):
    item = Uc.objects.get(id=pk)
    form = FormUc(instance = item)
    if request.method == 'POST':
        form = FormUc(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('ucs')     
    return render (request, 'asistencia/form_uc.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('asistencia.change_docente', raise_exception=True)
def editDocente(request, pk):
    item = Docente.objects.get(id=pk)
    form = FormDocente(instance = item)
    if request.method == 'POST':
        form = FormDocente(request.POST, instance = item)
        if form.is_valid():
            cap = form.save(commit=False)
            cap.nombre = cap.nombre.capitalize()
            cap.apellido = cap.apellido.capitalize()
            cap.save()
            return redirect('docentes')
            
    return render (request, 'asistencia/form_docente.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('asistencia.change_horario', raise_exception=True)
def editHorario(request, pk):
    item = Horario.objects.get(id=pk)
    form = FormHorario(instance = item)
    if request.method == 'POST':
        form = FormHorario(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('horarios')
            
    return render (request, 'asistencia/form_horario.html', {'form': form})
#--------------------------------------------------------------

#--------------------------------------------------------------delete
@login_required(login_url='/login/')
@permission_required('asistencia.delete_uc', raise_exception=True)
def deleteUc(request, pk):
    item = Uc.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('ucs')
    else:
        return render(request, 'errors/400.html', status=400) 

@login_required(login_url='/login/')
@permission_required('asistencia.delete_docente', raise_exception=True)
def deleteDocente(request, pk):
    item = Docente.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('docentes')
    else:
        return render(request, 'errors/400.html', status=400) 

@login_required(login_url='/login/')
@permission_required('asistencia.delete_horario', raise_exception=True)
def deleteHorario(request, pk):
    item = Horario.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('horarios')
    else:
        return render(request, 'errors/400.html', status=400) 
#--------------------------------------------------------------
