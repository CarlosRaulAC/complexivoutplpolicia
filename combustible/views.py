from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Combustible
from .forms import CombustibleForm
from django.views.generic import *

# Listar O Combustible
class CombustibleView(LoginRequiredMixin, generic.ListView):
    model = Combustible
    template_name = "combustible/orden_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CombustibleAdd(LoginRequiredMixin, CreateView):
    model = Combustible
    template_name = "combustible/orden_add.html"
    context_object_name = "obj"
    form_class = CombustibleForm
    success_url = reverse_lazy("combustible:orden_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CombustibleUpdate(LoginRequiredMixin,UpdateView):
    model = Combustible
    template_name = "combustible/orden_add.html"
    context_object_name = "obj"
    form_class = CombustibleForm
    success_url = reverse_lazy("combustible:orden_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar provincia
def combustible_inactivate(request, id):
    combustible = Combustible.objects.filter(pk=id).first()
    contexto = {}
    template_name = "combustible/orden_delete.html "

    if not combustible:
        return redirect("combustible:orden_list")
    
    if request.method=='GET':
        contexto = {'obj':combustible}

    if request.method=='POST':
        combustible.estado = False
        combustible.save()
        return redirect("combustible:orden_list")

    return render(request, template_name, contexto)
