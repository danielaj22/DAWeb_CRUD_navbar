from django.db import models

# Create your models here.
class  Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    puesto = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre
    