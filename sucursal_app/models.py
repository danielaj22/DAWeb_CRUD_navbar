from django.db import models

# Create your models here.
class Sucursales(models.Model):
    Id_Sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion  = models.CharField(max_length=100)
    horario   = models.CharField(max_length=50)
    telefono = models.CharField(max_length=100)
    email  = models.CharField( max_length=50)
    ciudad =  models.CharField( max_length=50)

    class Meta: 
        db_table =  "Sucursales"
        verbose_name = "Sucursale"
        verbose_name_plural = "Sucursales"

    def   __str__(self):
        return self.nombre