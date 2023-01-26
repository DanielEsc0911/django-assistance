# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path 
from django.conf import settings
from . import views

urlpatterns = [ 
    path('', views.indexHome, name = 'home' ),
    path('docentes', views.indexDocente, name ='docentes' ),
    path('docentes/crear', views.crearDocente, name ='crear_docente' ),
]
