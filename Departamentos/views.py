from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.http import HttpResponse
from .forms import DeptoForm, ContratoForm, InquilinoForm
from .models import Departamento, Inquilino, Contrato
from .utils import guardarArchivo

def home(request):
    return render(request, 'index.html')
    
class listarDepartamentos(ListView):
    model = Departamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class nuevoDepartamento(CreateView):
    template_name = 'Departamentos/departamento_form.html'
    form_class = DeptoForm
    success_url = '/gestion/'

class verDepartamento(DetailView):
    model = Departamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class editarDepartamento(UpdateView):
    model = Departamento
    form_class = DeptoForm
    success_url = '/gestion/'

# _____________________________________________________________________
    
class listarContratos(ListView):
    model = Contrato
    template_name = 'Contratos/contrato_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class nuevoContrato(CreateView):
    template_name = 'Contratos/contrato_form.html'
    form_class = ContratoForm
    success_url = '/gestion/'

class verContrato(DetailView):
    model = Contrato
    template_name = 'Contratos/contrato_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class editarContrato(UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'Contratos/contrato_form.html'
    success_url = '/gestion/'

# ______________________________________________________________________

class listarInquilinos(ListView):
    model = Inquilino
    template_name = 'Inquilinos/inquilino_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class nuevoInquilino(CreateView):
    template_name = 'Inquilinos/inquilino_form.html'
    form_class = InquilinoForm
    success_url = '/gestion/'

class verInquilino(DetailView):
    model = Inquilino
    template_name = 'Inquilinos/inquilino_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class editarInquilino(UpdateView):
    template_name = 'Inquilinos/inquilino_form.html'
    model = Inquilino
    form_class = InquilinoForm

# class subirFotos(FormView):
#     form_class = FileFieldForm
#     template_name = "upload.html"  # Replace with your template.
#     success_url = "home/"  # Replace with your URL or reverse().

#     def form_valid(self, form):
#         files = form.cleaned_data["file_field"]
#         for f in files:
#             guardarArchivo(f)
#         return super().form_valid(form)
        
        
