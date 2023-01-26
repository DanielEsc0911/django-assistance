from django import forms
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory
from django.forms import *
from .models import *


class FormDocente(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets ={
            'nombre': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'apellido': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'ci': Select(attrs={'class': 'form-select text-center'}),          
            'num_ci': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
        }

class FormHorario(ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets ={
            'uc': Select(attrs={'class': 'form-select'}),
            'dia': Select(attrs={'class': 'form-select'}),          
            'docente': Select(attrs={'class': 'form-select'}),          
            'entrada': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'salida':TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
        }

class FormUc(ModelForm):    
    class Meta:
        model = Uc
        fields = '__all__'
        widgets ={'nombre': TextInput(attrs={'class': 'form-control', 'autocomplete':'off'})}