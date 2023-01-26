import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

class Docente (models.Model):

    CI_OPT=(
        ('V', 'V'),
        ('E', 'E'),
    )
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    ci = models.CharField(max_length=1, choices=CI_OPT, blank=False, null=True)
    num_ci = models.CharField(max_length=8, validators=[RegexValidator(r'^[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+$')], blank=False, null=True)
    
    def __str__(self):
        nc = self.nombre + ' ' + self.apellido
        return nc

class Registro (models.Model):

    fecha = models.DateField(default=datetime.date.today, null=True)
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True)
    hora_de_entrada = models.DateField(blank=True, null=True)
    hora_de_salida = models.DateField(blank=True, null=True)