from urllib import request
from django import forms
from django.http import JsonResponse
from django.urls import reverse
from .models import ReclamoSugerencia
from dependencias.models import Circuito, Subcircuito
from dependencias.urls import *

class ReclamoSugerenciaForm(forms.ModelForm):

    tipo = forms.ChoiceField(
    choices=[('reclamo', 'Reclamo'), ('sugerencia', 'Sugerencia')],
    widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    detalle = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    contacto = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    nombres = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )


    class Meta:
        model = ReclamoSugerencia
        fields = ['circuito', 'subcircuito', 'tipo', 'detalle', 'contacto', 'nombres', 'apellidos']

    widgets = {
        'circuito': forms.Select(attrs={'class': 'form-control'}),
        'subcircuito': forms.Select(attrs={'class': 'form-control'}),
        'tipo': forms.Select(attrs={'class': 'form-control'}),
        'detalle': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
        'contacto': forms.TextInput(attrs={'class': 'form-control'}),
        'nombres': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),

    }
    

    def __init__(self, *args, **kwargs):
        super(ReclamoSugerenciaForm, self).__init__(*args, **kwargs)
        
        # Configurar campo circuito como ModelChoiceField
        self.fields['circuito'].queryset = Circuito.objects.all()
        self.fields['circuito'].widget.attrs['class'] = 'form-control select2'
        
        # Configurar campo subcircuito como ModelChoiceField
        self.fields['subcircuito'].queryset = Subcircuito.objects.all()  # Inicialmente vacío
        self.fields['subcircuito'].widget.attrs['class'] = 'form-control select2'

        # Añadir un atributo de datos para almacenar la URL de la vista AJAX
        self.fields['subcircuito'].widget.attrs['data-url'] = '{% url "dependencias:subcircuito_list" %}'


    def clean(self):
        cleaned_data = super().clean()
        circuito = cleaned_data.get('circuito')
        if circuito:
            # Filtrar opciones de subcircuito según el circuito seleccionado
            self.fields['subcircuito'].queryset = Subcircuito.objects.filter(circuito=circuito)
        return cleaned_data