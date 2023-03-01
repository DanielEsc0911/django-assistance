import django_filters
from django_filters import*
from django.forms import*
from .models import*


class AsistenciaFilter(django_filters.FilterSet):
    docente = ModelChoiceFilter(queryset = Docente.objects.all(), field_name="docente", widget=Select(attrs={'name':'search_docente', 'class':'form-control align-items-center', 'id':'id_dc'}))
    class Meta:
        model = Asistencia
        fields = (            
            'docente',
            )

class DocenteFilter(django_filters.FilterSet):
    nombre = CharFilter(field_name="nombre", lookup_expr="icontains", widget=TextInput(attrs={'name':'search_name', 'class':'form-control myform-search', 'placeholder':'Nombre', 'id':'s_nm'}))
    apellido = CharFilter(field_name="apellido", lookup_expr="icontains", widget=TextInput(attrs={'name':'search_name', 'class':'form-control myform-search', 'placeholder':'Apellido', 'id':'s_nm'}))
    class Meta:
        model = Docente
        fields = (            
            'nombre',
            'apellido',
            )

class HorarioFilter(django_filters.FilterSet):
    uc = ModelChoiceFilter(queryset = Uc.objects.all(), field_name="uc", widget=Select(attrs={'name':'search_uc', 'class':'form-control align-items-center', 'id':'id_uc'}))
    seccion = CharFilter(field_name="seccion", lookup_expr="icontains", widget=NumberInput(attrs={'name':'search_name', 'class':'form-control myform-search', 'placeholder':'Sec', 'id':'s_nm'}))
    class Meta:
        model = Horario
        fields = (            
            'uc',
            'seccion'
            )

class UcFilter(django_filters.FilterSet):
    nombre = CharFilter(field_name="nombre", lookup_expr="icontains", widget=TextInput(attrs={'name':'search_name', 'class':'form-control myform-search', 'placeholder':'Materia', 'id':'s_nm'}))
    class Meta:
        model = Uc
        fields = (            
            'nombre',
            )