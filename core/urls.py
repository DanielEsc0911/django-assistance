# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.asistencia.views import *
from apps.asistencia.utils import *

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    # ADD NEW Routes HERE
    
    # Leave `Home.Urls` as last the last line
    path("", include("apps.asistencia.urls"))
]

handler400 = "apps.asistencia.utils.page_400"
handler403 = "apps.asistencia.utils.page_403"
handler404 = "apps.asistencia.utils.page_404"
handler500 = "apps.asistencia.utils.page_500"