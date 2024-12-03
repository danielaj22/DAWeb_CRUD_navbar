from django.db import models

# Create your models here.
class  Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    tipo_producto = models.CharField(max_length=45)
    lote = models.IntegerField()
    marca =models.CharField(max_length=60)
    id_sucursal = models.CharField(max_length=6)

    def __str__(self):
        return self.nombre