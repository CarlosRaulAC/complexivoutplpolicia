from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Provincia, Distrito, Canton, Circuito, Subcircuito
from .forms import ProvinciaForm, DistritoForm, CantonForm, CircuitoForm, SubcircuitoForm
from django.urls import reverse_lazy


# Create your views here.
# Vistas para Provincia
class ProvinciaView(LoginRequiredMixin, ListView):
    template_name = "dependencias/provincia_list.html"
    login_url = 'bases:login'
    model = Provincia
    context_object_name = "obj"

class ProvinciaAdd(LoginRequiredMixin, CreateView):
    model = Provincia
    template_name = "dependencias/provincia_add.html"
    context_object_name = "obj"
    form_class = ProvinciaForm
    success_url = reverse_lazy("dependencias:provincia_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ProvinciaUpdate(LoginRequiredMixin,UpdateView):
    model = Provincia
    template_name = "dependencias/provincia_add.html"
    context_object_name = "obj"
    form_class = ProvinciaForm
    success_url = reverse_lazy("dependencias:provincia_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar provincia
def provincia_inactivate(request, id):
    provincia = Provincia.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not provincia:
        return redirect("dependencias:provincia_list")
    
    if request.method=='GET':
        contexto = {'obj':provincia} 

    if request.method=='POST':
        provincia.estado = False
        provincia.save()
        return redirect("dependencias:provincia_list")

    return render(request, template_name, contexto)


# Vistas para Distrito
class DistritoView(LoginRequiredMixin, ListView):
    template_name = "dependencias/distrito_list.html"
    login_url = 'bases:login'
    model = Distrito
    context_object_name = "obj"

class DistritoAdd(LoginRequiredMixin, CreateView):
    model = Distrito
    template_name = "dependencias/distrito_add.html"
    context_object_name = "obj"
    form_class = DistritoForm
    success_url = reverse_lazy("dependencias:distrito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class DistritoUpdate(LoginRequiredMixin,UpdateView):
    model = Distrito
    template_name = "dependencias/distrito_add.html"
    context_object_name = "obj"
    form_class = DistritoForm
    success_url = reverse_lazy("dependencias:distrito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar provincia
def distrito_inactivate(request, id):
    distrito = Distrito.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not distrito:
        return redirect("dependencias:distrito_list")
    
    if request.method=='GET':
        contexto = {'obj':distrito}

    if request.method=='POST':
        distrito.estado = False
        distrito.save()
        return redirect("dependencias:distrito_list")

    return render(request, template_name, contexto)

#Vistas para Cantones
class CantonView(LoginRequiredMixin, ListView):
    template_name = "dependencias/canton_list.html"
    login_url = 'bases:login'
    model = Canton
    context_object_name = "obj"

class CantonAdd(LoginRequiredMixin, CreateView):
    model = Canton
    template_name = "dependencias/canton_add.html"
    context_object_name = "obj"
    form_class = CantonForm
    success_url = reverse_lazy("dependencias:canton_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CantonUpdate(LoginRequiredMixin,UpdateView):
    model = Canton
    template_name = "dependencias/canton_add.html"
    context_object_name = "obj"
    form_class = CantonForm
    success_url = reverse_lazy("dependencias:canton_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar canton
def canton_inactivate(request, id):
    canton = Canton.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not canton:
        return redirect("dependencias:canton_list")
    
    if request.method=='GET':
        contexto = {'obj':canton}

    if request.method=='POST':
        canton.estado = False
        canton.save()
        return redirect("dependencias:canton_list")

    return render(request, template_name, contexto)

#Vistas para Circuitos
class CircuitoView(LoginRequiredMixin, ListView):
    template_name = "dependencias/circuito_list.html"
    login_url = 'bases:login'
    model = Circuito
    context_object_name = "obj"

class CircuitoAdd(LoginRequiredMixin, CreateView):
    model = Circuito
    template_name = "dependencias/circuito_add.html"
    context_object_name = "obj"
    form_class = CircuitoForm
    success_url = reverse_lazy("dependencias:circuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CircuitoUpdate(LoginRequiredMixin,UpdateView):
    model = Circuito
    template_name = "dependencias/circuito_add.html"
    context_object_name = "obj"
    form_class = CircuitoForm
    success_url = reverse_lazy("dependencias:circuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar canton
def circuito_inactivate(request, id):
    circuito = Circuito.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not circuito:
        return redirect("dependencias:circuito_list")
    
    if request.method=='GET':
        contexto = {'obj':circuito}

    if request.method=='POST':
        circuito.estado = False
        circuito.save()
        return redirect("dependencias:circuito_list")

    return render(request, template_name, contexto)


#Vistas para Subcircuitos
class SubcircuitoView(LoginRequiredMixin, ListView):
    template_name = "dependencias/subcircuito_list.html"
    login_url = 'bases:login'
    model = Subcircuito
    context_object_name = "obj"

class SubcircuitoAdd(LoginRequiredMixin, CreateView):
    model = Subcircuito
    template_name = "dependencias/subcircuito_add.html"
    context_object_name = "obj"
    form_class = SubcircuitoForm
    success_url = reverse_lazy("dependencias:subcircuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class SubcircuitoUpdate(LoginRequiredMixin,UpdateView):
    model = Subcircuito
    template_name = "dependencias/subcircuito_add.html"
    context_object_name = "obj"
    form_class = SubcircuitoForm
    success_url = reverse_lazy("dependencias:subcircuito_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
# Vista de función para inactivar canton
def subcircuito_inactivate(request, id):
    subcircuito = Subcircuito.objects.filter(pk=id).first()
    contexto = {}
    template_name = "dependencias/dependencias_delete.html "

    if not subcircuito:
        return redirect("dependencias:subcircuito_list")
    
    if request.method=='GET':
        contexto = {'obj':subcircuito}

    if request.method=='POST':
        subcircuito.estado = False
        subcircuito.save()
        return redirect("dependencias:subcircuito_list")

    return render(request, template_name, contexto)

