#Formularios para Modelo Personal
from django import forms
from .models import Personal
from catalogos.models import Rango


class PersonalForm(forms.ModelForm):

    rango = forms.ModelChoiceField(
        queryset=Rango.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    estado = forms.ChoiceField(
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    class Meta:
        model = Personal
        fields = ['rango', 'cedula', 'nombres_apellidos', 'f_nac', 't_sangre', 'ciudad_nacimiento', 'celular', 'estado']
        labels = {
            'rango': "Rango",
            'cedula': "Cédula",
            'nombres_apellidos': "Nombres y Apellidos",
            'f_nac': "Fecha de Nacimiento",
            't_sangre': "Tipo de Sangre",
            'ciudad_nacimiento': "Ciudad de Nacimiento",
            'celular': "Número de Celular",
            'estado': "Estado"
        }
        widgets = {
            'rango': forms.Select(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cédula'}),
            'nombres_apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombres y apellidos'}),
            'f_nac': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}),
            't_sangre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de sangre'}),
            'ciudad_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad de nacimiento'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de celular'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['rango'].empty_label = "Rango"
