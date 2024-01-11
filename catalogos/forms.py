from django import forms
from .models import Rango, Tipo_Vehiculo, Tipo_Mantenimiento

class RangoForm(forms.ModelForm):
    class Meta:
        model = Rango
        fields = ['nombre','estado']
        labels = {'nombre':"Nombre de Rango",'estado':"Estado"}
        widget = {'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Vehiculo
        fields = ['nombre','estado']
        labels = {'nombre':"Nombre de Vehiculo",'estado':"Estado"}
        widget = {'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class TipoMantenimientoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Mantenimiento
        fields = ['nombre','estado']
        labels = {'nombre':"Nombre de Mantenimiento",'estado':"Estado"}
        widget = {'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
