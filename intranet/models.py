from django.db import models

class Persona(models.Model):
    
    rut = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=100)
    nacimiento = models.DateField()
    telefono = models.IntegerField()
    contrasenia = models.CharField(max_length=100)
    def __str__(self):
        return "PERSONA"

class Subscripcion(models.Model):
    email = models.EmailField(max_length=100)
    def __str__(self):
        return "SUBSCRIPCION"

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    contacto = models.CharField(max_length=100)
    def __str__(self):
        return "AVISO"
      

