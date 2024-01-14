from django import forms
from .models import *

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['codigo','nombre','estado']
        labels = {'codigo':"Código de Provincia",'nombre':"Nombre de Provincia",'estado':"Estado"}
        widget = {'codigo': forms.TextInput,'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProvinciaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre

class DistritoForm(forms.ModelForm):
    provincia = forms.ModelChoiceField(
        queryset=Provincia.objects.filter(estado=True).order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
        to_field_name='nombre'
    )

    estado = forms.ChoiceField(
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    class Meta:
        model = Distrito
        fields = ['provincia', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código', 'style': 'margin-bottom: 10px;'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre', 'style': 'margin-bottom: 10px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'margin-bottom: 10px;'
            })
        self.fields['provincia'].empty_label = "Provincia"


class CantonForm(forms.ModelForm):
    distrito = forms.ModelChoiceField(
        queryset=Distrito.objects.filter(estado=True).order_by('codigo'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    estado = forms.ChoiceField(
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    class Meta:
        model = Canton
        fields = ['distrito', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['distrito'].empty_label = "Distrito"

class CircuitoForm(forms.ModelForm):
    canton = forms.ModelChoiceField(
        queryset=Canton.objects.filter(estado=True).order_by('codigo'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    estado = forms.ChoiceField(
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    class Meta:
        model = Circuito
        fields = ['canton', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['canton'].empty_label = "Canton"

class SubcircuitoForm(forms.ModelForm):
    circuito = forms.ModelChoiceField(
        queryset=Circuito.objects.filter(estado=True).order_by('codigo'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    estado = forms.ChoiceField(
        choices=[(True, 'Activo'), (False, 'Inactivo')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
    )

    class Meta:
        model = Subcircuito
        fields = ['circuito', 'codigo', 'nombre', 'estado']
        labels = {'codigo': "Código", 'nombre': "Nombre", 'estado': "Estado"}
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['circuito'].empty_label = "Circuito"