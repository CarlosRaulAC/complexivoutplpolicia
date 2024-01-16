from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from dependencias.models import Subcircuito
from .models import ReclamoSugerencia
from .forms import ReclamoSugerenciaForm
from django.urls import reverse_lazy


# Create your views here.
#Vista para crear Reclamos y sugerencias
class ReclamoSugerenciaAdd(CreateView):

    model = ReclamoSugerencia
    template_name = "reclamosugerencia/reclamosugerencia_add.html"
    context_object_name = "obj"
    form_class = ReclamoSugerenciaForm
    success_url = reverse_lazy("home:login")
    login_url = 'bases:login'


    def form_valid(self, form):
        return super().form_valid(form)
    
# Vistas para Reclamos y Sugerencias
class ReclamoSugerenciaView(LoginRequiredMixin, ListView):
    template_name = "reclamosugerencia/reclamosugerencia_list.html"
    login_url = 'bases:login'
    model = ReclamoSugerencia
    context_object_name = "obj"
