from django.db import models
from django.views import generic

class Persona(models.Model):
    
    rut = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=100)
    nacimiento = models.DateField()
    telefono = models.IntegerField()
    contrasenia = models.CharField(max_length=100)
    def __str__(self):
        return "PERSONA"

class Suscripcion(models.Model):
    email = models.EmailField(max_length=100)
    def __str__(self):
        return "SUSCRIPCION"

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    emailcontacto = models.EmailField(max_length=100)
    contacto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    
    def __str__(self):
        return "AVISO"



