from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q


# Create your models here.

class Departamento(models.Model):
    alquilado = models.BooleanField()
    calle = models.CharField(max_length=20)
    altura = models.CharField(max_length=4)
    edificio = models.CharField(max_length=20)
    piso = models.CharField(max_length=10)
    division = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=60)

class Reserva(models.Model):
    dia_inicial = models.DateField(auto_now=False)
    dia_final =  models.DateField(auto_now=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null = True, blank = True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    residencia = models.CharField(max_length=20)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    
