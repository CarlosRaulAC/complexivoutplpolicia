from django.db import models
from personal.models import Personal
from flota.models import FlotaVehicular
from dependencias.models import Subcircuito
from home.models import ClaseBase

# Create your models here.
class Combustible(models.Model):
    galones = models.CharField(max_length=50)
    fecha_abastecimiento = models.DateTimeField()
    hora = models.TimeField()
    kilometraje = models.CharField(max_length=20,)
    conductor = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='movilizacion_conductor1')
    vehiculo = models.ForeignKey(FlotaVehicular, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='movilizacion_solicitante1')
    subcircuito = models.ForeignKey(Subcircuito, on_delete=models.CASCADE)
    gasolinera = models.CharField(max_length=50)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return '{}:{}'.format(self.vehiculo, self.conductor)
    
    def save(self, *args, **kwargs):
        self.gasolinera = self.gasolinera.upper()
        
        # Agrega las demás conversiones a mayúsculas para los campos necesarios
        super(Combustible, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Movilizacioness"