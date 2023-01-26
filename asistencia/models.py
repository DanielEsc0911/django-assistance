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

class Horario (models.Model):
    DAY_OPT=(
        ('LUN','Lunes'),
        ('MAR','Martes'),
        ('MIE','Miércoles'),
        ('JUE','Jueves'),
        ('VIE','Viernes'),
        ('SAB','Sábado'),
        ('DOM','Domingo'),
    )
    dia = models.CharField(max_length=10, choices=DAY_OPT, blank=False, null=True)
    uc = models.ForeignKey('Uc', on_delete=models.RESTRICT, null=True)
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True)
    entrada = models.DateField(blank=True, null=True)
    salida = models.DateField(blank=True, null=True)

class Uc (models.Model):
    nombre = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Unidad Curricular'
        verbose_name_plural = 'Unidades Curriculares'

    def __str__(self):       
        return self.nombre