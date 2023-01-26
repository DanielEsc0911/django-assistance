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
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido': TextInput(attrs={'class': 'form-control' }),
            'ci': Select(attrs={'class': 'form-control text-center'}),          
            'num_ci': TextInput(attrs={'class': 'form-control'}),
        }