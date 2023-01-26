from django.contrib import admin
from .models import *


class DocenteAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    list_display = ('nombre', 'apellido', 'ci', 'num_ci')

class RegistroAdmin(admin.ModelAdmin):
    ordering = ('fecha',)
    list_display = ('fecha', 'docente', 'entrada', 'salida')
    
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Uc)