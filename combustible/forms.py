from django import forms
from .models import Combustible
from personal.models import Personal
from flota.models import FlotaVehicular
from dependencias.models import Subcircuito

class CombustibleForm(forms.ModelForm):
    conductor = forms.ModelChoiceField(
        queryset=Personal.objects.filter(estado=True).order_by('nombres_apellidos'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    vehiculo = forms.ModelChoiceField(
        queryset=FlotaVehicular.objects.filter(estado=True).order_by('tipovehiculo'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    solicitante = forms.ModelChoiceField(
        queryset=Personal.objects.filter(estado=True).order_by('nombres_apellidos'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subcircuito = forms.ModelChoiceField(
        queryset=Subcircuito.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Combustible
        fields = ['galones', 'fecha_abastecimiento', 'hora', 'kilometraje', 'conductor', 'vehiculo',
                  'solicitante', 'subcircuito', 'gasolinera']
        labels = {
            'galones': "Cantidad de Galones",
            'fecha_abastecimiento': "Fecha de Abastecimiento",
            'hora': "Hora",
            'kilometraje': "Kilometraje",
            'conductor': "Conductor",
            'vehiculo': "Vehiculo",
            'solicitante': "Solicitante",
            'subcircuito': "Subcircuito",
            'gasolinera': "Nombre de la Gasolinera",
        }
        label_suffix = ""
        widgets = {
            'galones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese cantidad de galones'}),
            'fecha_abastecimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha de abastecimiento'}),
            'hora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la hora'}),
            'kilometraje': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el kilometraje'}),
            'gasolinera': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la gasolinera'}),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'