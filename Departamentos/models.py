from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    foto = models.ImageField(upload_to="uploads/Departamentos",blank=True,null=True)
    ubicacion = models.TextField(max_length=30)
    cantHabitaciones = models.IntegerField()
    mobiliario = models.TextField(max_length=300,blank=True, null=True)
    servicios = models.TextField(max_length=200,blank=True, null=True)
    estadoInicial = models.TextField(max_length=300,blank=True, null=True)
    valor = models.IntegerField()

    def __str__(self):
        return f'{self.ubicacion} {self.cantHabitaciones} {self.mobiliario} {self.servicios} {self.estadoInicial}'

class Inquilino(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    telefonoAlt = models.IntegerField(blank=True,null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.dni} {self.telefono} {self.user.email} {self.departamento}'

class Contrato(models.Model):
    pdf = models.FileField(upload_to="uploads/Contratos")
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    monto = models.PositiveBigIntegerField()
    inicio = models.DateField()
    pago = models.DateField(blank=True,null=True)
    mantenimiento = models.TextField(max_length=500, blank=True,null=True)
    cancelacion = models.TextField(blank=True,null=True)
    pautas = models.TextField(max_length=300,blank=True,null=True)
    aumentos = models.IntegerField() # en porcentaje

    def __str__(self):
        return f'{self.pdf} {self.inquilino} {self.monto} {self.inicio} {self.pago} {self.mantenimiento} {self.aumentos} {self.cancelacion} {self.pautas}'

class fotosDepartamento(models.Model):
    foto = models.ImageField(upload_to="uploads/")
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
