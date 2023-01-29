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
    num_ci = models.CharField(max_length=8, validators=[RegexValidator(r'^[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+$')], unique=True, null=True)

    def __str__(self):
        nc = self.nombre + ' ' + self.apellido
        return nc

class Horario (models.Model):
    DIA_OPT=(
        ('1Lunes','Lunes'),
        ('2Martes','Martes'),
        ('3Miércoles','Miércoles'),
        ('4Jueves','Jueves'),
        ('5Viernes','Viernes'),
        ('6Sábado','Sábado'),
        ('7Domingo','Domingo'),
    )
    uc = models.ForeignKey('Uc', on_delete=models.RESTRICT, null=True)
    seccion = models.IntegerField(validators=[int_list_validator(allow_negative=False)], null=True)
    docente = models.ForeignKey('Docente', on_delete=models.SET_NULL, null=True)
    dia = models.CharField(max_length=10, choices=DIA_OPT, blank=False, null=True)
    entrada = models.CharField(max_length=5, validators=[RegexValidator(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')], blank=True, null=True)
    salida = models.CharField(max_length=5, validators=[RegexValidator(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')], blank=True, null=True)

class Uc (models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=True)

    class Meta:
        verbose_name = 'Unidad Curricular'
        verbose_name_plural = 'Unidades Curriculares'

    def __str__(self):       
        return self.nombre

class Asistencia (models.Model):
    fecha = models.DateField(null=True)
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True)
    asistencia = models.BooleanField(null=True)
