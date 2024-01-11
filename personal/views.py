from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from personal.forms import PersonalForm
from .models import Personal

# Create your views here.
# Vistas para Provincia
class PersonalView(LoginRequiredMixin, ListView):
    template_name = "personal/personal_list.html"
    login_url = 'bases:login'
    model = Personal
    context_object_name = "obj"

class PersonalAdd(LoginRequiredMixin, CreateView):
    model = Personal
    template_name = "personal/personal_add.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("personal:policial_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class PersonalUpdate(LoginRequiredMixin,UpdateView):
    model = Personal
    template_name = "personal/personal_add.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("personal:policial_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar provincia
def personal_inactivate(request, id):
    personal = Personal.objects.filter(pk=id).first()
    contexto = {}
    template_name = "personal/personal_delete.html "

    if not personal:
        return redirect("personal:policial_list")
    
    if request.method=='GET':
        contexto = {'obj':personal}

    if request.method=='POST':
        personal.estado = False
        personal.save()
        return redirect("personal:policial_list")

    return render(request, template_name, contexto)