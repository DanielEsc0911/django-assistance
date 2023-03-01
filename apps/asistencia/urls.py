from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path 
from django.conf import settings
from . import views

urlpatterns = [ 
    path('', views.Redir, name = 'redir'),
    path('home', views.indexHome, name = 'home'),

    path('ucs', views.indexUc, name ='ucs'),
    path('docentes', views.indexDocente, name ='docentes'),
    path('horarios', views.indexHorario, name ='horarios'),
    path('asistencias', views.indexAsistencia, name ='asistencias'), #path('asistencias/docente/<str:pk>', views.indexAsistenciaDocente, name ='asistencias_docente'),

    path('ucs/crear', views.crearUc, name ='crear_uc'),
    path('docentes/crear', views.crearDocente, name ='crear_docente'),
    path('horarios/crear', views.crearHorario, name ='crear_horario'),
    path('asistencias/crear', views.crearAsistencia, name ='crear_asistencia'),
    
    path('ucs/<str:pk>/edit', views.editUc, name ='edit_uc'),
    path('docentes/<str:pk>/edit', views.editDocente, name ='edit_docente'),
    path('horarios/<str:pk>/edit', views.editHorario, name ='edit_horario'),
    #path('asistencia/<str:pk>/edit', views.editAsistencia, name ='edit_asistencia'),
    
    path('ucs/<str:pk>/delete', views.deleteUc, name ='delete_uc'),
    path('docentes/<str:pk>/delete', views.deleteDocente, name ='delete_docente'),
    path('horarios/<str:pk>/delete', views.deleteHorario, name ='delete_horario'),
    #path('asistencia/<str:pk>/delete', views.deleteAsistencia, name ='delete_asistencia'),
]
