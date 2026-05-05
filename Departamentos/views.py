from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import DeptoForm, ContratoForm, InquilinoForm, FileFieldForm, UserForm
from .models import Departamento, Inquilino, Contrato, fotosDepartamento
from .utils import guardarArchivo

def home(request):
    return render(request, 'index.html')

class listarDepartamentos(PermissionRequiredMixin, ListView):
    model = Departamento
    permission_required = "ComerPiza"

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

class subirFoto(FormView):
    model = fotosDepartamento
    form_class = FileFieldForm
    template_name = "Departamentos/departamento_form.html"  # Replace with your template.
    success_url = "/gestion/"  # Replace with your URL or reverse().

    def form_valid(self, form):
        fotos = form.cleaned_data["fotos"]
        departamento = form.cleaned_data["departamento"]

        for f in fotos:
            fotosDepartamento.objects.create(foto=f,departamento=departamento)
        return super().form_valid(form)

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

class registrarInquilino(CreateView):

    def get(self, request):
        user_form = UserForm()
        inquilino_form = InquilinoForm()
        return render(request, 'Inquilinos/inquilino_form.html', {
            'user_form': user_form,
            'inquilino_form': inquilino_form
        })

    def post(self, request):
        user_form = UserForm(request.POST)
        inquilino_form = InquilinoForm(request.POST)

        if user_form.is_valid() and inquilino_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            inquilino = inquilino_form.save(commit=False)
            inquilino.user = user
            inquilino.save()

            return redirect('home')

        return render(request, 'Inquilinos/inquilino_form.html', {
            'user_form': user_form,
            'inquilino_form': inquilino_form
        })