from django.db import models
from personal.models import Personal
from flota.models import FlotaVehicular
from dependencias.models import Subcircuito
from home.models import ClaseBase

# Create your models here.
class Movilizacion(models.Model):
    motivo = models.CharField(max_length=50)
    fecha_salida = models.DateTimeField()
    hora = models.TimeField()
    ruta = models.CharField(max_length=50)
    kilometraje = models.CharField(max_length=20,)
    conductor = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='movilizacion_conductor')
    vehiculo = models.ForeignKey(FlotaVehicular, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='movilizacion_solicitante')
    subcircuito = models.ForeignKey(Subcircuito, on_delete=models.CASCADE)
    numero_ocupantes = models.IntegerField()
    datos_ocupantes = models.CharField(max_length=250)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return '{}:{}'.format(self.motivo, self.conductor)
    
    def save(self, *args, **kwargs):
        self.motivo = self.motivo.upper()
        self.ruta = self.ruta.upper()
        self.datos_ocupantes = self.datos_ocupantes.upper()
        # Agrega las demás conversiones a mayúsculas para los campos necesarios
        super(Movilizacion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Movilizaciones"