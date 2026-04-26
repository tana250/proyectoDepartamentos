from django.db import models

class Departamento(models.Model):
    foto = models.ImageField(upload_to="uploads/Departamentos",blank=True,null=True)
    ubicacion = models.CharField(max_length=30)
    cantHabitaciones = models.IntegerField()
    mobiliario = models.CharField(max_length=300)
    servicios = models.CharField(max_length=200)
    estadoInicial = models.CharField(max_length=300)
    valor = models.IntegerField()

    def __str__(self):
        return f'{self.ubicacion} {self.cantHabitaciones} {self.mobiliario} {self.servicios} {self.estadoInicial}'

class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField() 
    telefonoAlt = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.dni} {self.telefono} {self.email} {self.telefonoAlt} {self.departamento}'


class Contrato(models.Model):
    pdf = models.FileField(upload_to="uploads/Contratos",blank=True,null=True)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    monto = models.PositiveBigIntegerField()
    inicio = models.DateField()
    pago = models.DateField()
    mantenimiento = models.CharField(max_length=500)
    cancelacion = models.CharField(null=True)
    pautas = models.CharField(max_length=300, null=True)
    aumentos = models.IntegerField()

    def __str__(self):
        return f'{self.pdf} {self.inquilino} {self.monto} {self.inicio} {self.pago} {self.mantenimiento} {self.aumentos} {self.cancelacion} {self.pautas}'

class fotosDepartamento(models.Model):
    foto = models.ImageField(upload_to="uploads/")
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
