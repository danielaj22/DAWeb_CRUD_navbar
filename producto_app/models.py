from django.db import models

# Create your models here.
class  Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=11)
    tipo_producto = models.CharField(max_length=45)
    lote = models.IntegerField(max_length=15)
    marca =models.CharField(max_length=60)

    def __str__(self):
        return self.nombre