from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Rango, Tipo_Vehiculo, Tipo_Mantenimiento
from .forms import RangoForm, TipoVehiculoForm, TipoMantenimientoForm
from django.urls import reverse_lazy

# Create your views here.
# Vista para listar o ver tipos de vehiculos
class Tipo_VehiculoView(LoginRequiredMixin, ListView):
    template_name = "catalogos/tipo_vehiculo_list.html"
    login_url = 'bases:login'
    model = Tipo_Vehiculo
    context_object_name = "obj"

# Vista de para Crear Tipos de Vehiculos
class Tipo_VehiculoAdd(LoginRequiredMixin, CreateView):
    template_name = "catalogos/tipo_vehiculo_add.html"
    login_url = 'bases:login'
    model = Tipo_Vehiculo
    form_class = TipoVehiculoForm
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:tipo_vehiculo_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Vista de clase para editar Tipos de Vehiculos 
class Tipo_VehiculoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "catalogos/tipo_vehiculo_add.html"
    login_url = 'bases:login'
    form_class = TipoVehiculoForm
    model = Tipo_Vehiculo
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:tipo_vehiculo_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar tipos de vehiculos
def tipo_vehiculo_inactivate(request, id):
    tipo_vehiculo = Tipo_Vehiculo.objects.filter(pk=id).first()
    contexto = {}
    template_name = "catalogos/catalogos_delete.html "

    if not tipo_vehiculo:
        return redirect("catalogos:tipo_vehiculo_list")
    
    if request.method=='GET':
        contexto = {'obj':tipo_vehiculo}

    if request.method=='POST':
        tipo_vehiculo.estado = False
        tipo_vehiculo.save()
        return redirect("catalogos:tipo_vehiculo_list")

    return render(request, template_name, contexto)

# Vista para listar o ver tipos de mantenimientos
class Tipo_MantenimientoView(LoginRequiredMixin, ListView):
    template_name = "catalogos/tipo_mantenimiento_list.html"
    login_url = 'bases:login'
    model = Tipo_Mantenimiento
    context_object_name = "obj"

# Vista de para Crear Tipos de Mantenimiento
class Tipo_MantenimientoAdd(LoginRequiredMixin, CreateView):
    template_name = "catalogos/tipo_mantenimiento_add.html"
    login_url = 'bases:login'
    model = Tipo_Mantenimiento
    form_class = TipoMantenimientoForm
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:tipo_mantenimiento_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Vista de clase para editar Tipos de Mantenimiento
class Tipo_MantenimientoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "catalogos/tipo_mantenimiento_add.html"
    login_url = 'bases:login'
    form_class = TipoMantenimientoForm
    model = Tipo_Mantenimiento
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:tipo_mantenimiento_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar tipos de mantenimiento
def tipo_mantenimiento_inactivate(request, id):
    tipo_mantenimiento = Tipo_Mantenimiento.objects.filter(pk=id).first()
    contexto = {}
    template_name = "catalogos/catalogos_delete.html "

    if not tipo_mantenimiento:
        return redirect("catalogos:tipo_mantenimiento_list")
    
    if request.method=='GET':
        contexto = {'obj':tipo_mantenimiento}

    if request.method=='POST':
        tipo_mantenimiento.estado = False
        tipo_mantenimiento.save()
        return redirect("catalogos:tipo_mantenimiento_list")

    return render(request, template_name, contexto)   
       
# Vista para listar o ver rangos
class RangoView(LoginRequiredMixin, ListView):
    template_name = "catalogos/rango_list.html"
    login_url = 'bases:login'
    model = Rango
    context_object_name = "obj"
    
# Vista de para Crear Rangos
class RangoAdd(LoginRequiredMixin, CreateView):
    template_name = "catalogos/rango_add.html"
    login_url = 'bases:login'
    model = Rango
    form_class = RangoForm
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:rango_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

# Vista de clase para editar Rangos 
class RangoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "catalogos/rango_add.html"
    login_url = 'bases:login'
    form_class = RangoForm
    model = Rango
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:rango_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

# Vista de función para inactivar rangos
def rango_inactivate(request, id):
    rango = Rango.objects.filter(pk=id).first()
    contexto = {}
    template_name = "catalogos/catalogos_delete.html "

    if not rango:
        return redirect("catalogos:rango_list")
    
    if request.method=='GET':
        contexto = {'obj':rango}

    if request.method=='POST':
        rango.estado = False
        rango.save()
        return redirect("catalogos:rango_list")

    return render(request, template_name, contexto)    

    
