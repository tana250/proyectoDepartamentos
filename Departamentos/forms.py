from .models import Departamento, Inquilino, Contrato
from django.contrib.auth.models import User
from django import forms

class DeptoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ["foto", "ubicacion", "cantHabitaciones", "mobiliario", "servicios", "estadoInicial", "valor"]


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ["pdf", "inquilino", "monto", "inicio", "pago", "mantenimiento", "aumentos", "pautas", "cancelacion",]
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'pago': forms.DateInput(attrs={'type': 'date'}),
        }

class InquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = ["user", "dni", "telefono", "telefonoAlt", "departamento"]


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class FileFieldForm(forms.Form):
    fotos = MultipleFileField()
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all())
