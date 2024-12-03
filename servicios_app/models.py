from django.db import models

# Create your models here.
class Servicios(models.Model):
    Id_Servicio = models.IntegerField(primary_key=True)
    Id_cliente  = models.IntegerField()
    Id_Empleado  = models.IntegerField()
    tipo =  models.CharField(max_length=50)
    precio  = models.CharField(max_length=50)
    fecha_serv = models.DateField()

    class Meta: 
        db_table =  "Servicios"
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def    __str__(self):
        return self.Id_Servicio