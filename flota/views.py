from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import FlotaVehicular
from django.urls import reverse_lazy
from .forms import FlotaVehicularForm

# Vistas para Flota vehicular
class FlotaVehicularView(LoginRequiredMixin, ListView):
    template_name = "flota/flota_list.html"
    login_url = 'bases:login'
    model = FlotaVehicular
    context_object_name = "obj"

class FlotaVehicularAdd(LoginRequiredMixin, CreateView):
    model = FlotaVehicular
    template_name = "flota/flota_add.html"
    context_object_name = "obj"
    form_class = FlotaVehicularForm
    success_url = reverse_lazy("flota:vehicular_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class FlotaVehicularUpdate(LoginRequiredMixin,UpdateView):
    model = FlotaVehicular
    template_name = "flota/flota_add.html"
    context_object_name = "obj"
    form_class = FlotaVehicularForm
    success_url = reverse_lazy("flota:vehicular_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar vehiculo
def flotavehicular_inactivate(request, id):
    flotavehicular = FlotaVehicular.objects.filter(pk=id).first()
    contexto = {}
    template_name = "flota/flota_delete.html"

    if not flotavehicular:
        return redirect("flota:vehicular_list")
    
    if request.method=='GET':
        contexto = {'obj':flotavehicular}

    if request.method=='POST':
        flotavehicular.estado = False
        flotavehicular.save()
        return redirect("flota:vehicular_list")

    return render(request, template_name, contexto)