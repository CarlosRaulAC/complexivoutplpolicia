#Formularios para Modelo Flota Vehicular
from django import forms
from .models import FlotaVehicular
from catalogos.models import Tipo_Vehiculo

class FlotaVehicularForm(forms.ModelForm):
    tipovehiculo = forms.ModelChoiceField(
        queryset=Tipo_Vehiculo.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    estado = forms.ChoiceField(
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    class Meta:
        model = FlotaVehicular
        fields = ['tipovehiculo', 'placa', 'chasis', 'marca', 'modelo', 'motor', 'kilometraje',
                  'cilindraje', 'capacidad_carga', 'capacidad_pasajeros', 'estado']
        labels = {
            'tipovehiculo': "Tipo de Vehículo",
            'placa': "Placa",
            'chasis': "Chasis",
            'marca': "Marca",
            'modelo': "Modelo",
            'motor': "Motor",
            'kilometraje': "Kilometraje",
            'cilindraje': "Cilindraje",
            'capacidad_carga': "Capacidad de Carga",
            'capacidad_pasajeros': "Capacidad de Pasajeros",
            'estado': "Estado"
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la placa'}),
            'chasis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el chasis'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el modelo'}),
            'motor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el motor'}),
            'kilometraje': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el kilometraje'}),
            'cilindraje': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el cilindraje'}),
            'capacidad_carga': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de carga'}),
            'capacidad_pasajeros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de pasajeros'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['tipovehiculo'].empty_label = "Tipo de Vehiculo"
