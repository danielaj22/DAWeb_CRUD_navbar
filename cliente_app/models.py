from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    apellidoP = models.CharField(max_length=45)
    apellidoM = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    cuenta = models.CharField(max_length=20)


    def __str__(self):
        return self.nombre
    
   