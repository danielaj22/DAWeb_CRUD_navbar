from django.db import models

# Create your models here.
class  Proveedores(models.Model):
    id_proveedor = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    