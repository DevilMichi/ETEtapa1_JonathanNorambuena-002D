from django.db import models

# Create your models here.
class Proveedor(models.Model):
    IDE = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=70)
    Email = models.CharField(max_length=40)
    Pais = models.CharField(max_length=10)
    Contraseña = models.CharField(max_length=15)
    def __str__(self):
         return self.Nombre
