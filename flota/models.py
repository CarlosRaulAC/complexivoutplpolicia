from django.db import models
from catalogos.models import Tipo_Vehiculo
from home.models import ClaseBase

class FlotaVehicular(ClaseBase):
    tipovehiculo = models.ForeignKey(Tipo_Vehiculo, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10, help_text='', unique=True)
    chasis = models.CharField(max_length=30, help_text='', unique=True)
    marca = models.CharField(max_length=20, help_text='')
    modelo = models.CharField(max_length=30, help_text='')
    motor = models.CharField(max_length=20, help_text='')
    kilometraje = models.CharField(max_length=20, help_text='')
    cilindraje = models.CharField(max_length=20, help_text='')
    capacidad_carga = models.CharField(max_length=20, help_text='')
    capacidad_pasajeros = models.CharField(max_length=20, help_text='')

    def __str__(self):
        return '{}:{}'.format(self.tipovehiculo, self.placa)

    def save(self, *args, **kwargs):
        self.marca = self.marca.upper()
        self.modelo = self.modelo.upper()
        self.motor = self.motor.upper()
        # Agrega las demás conversiones a mayúsculas para los campos necesarios
        super(FlotaVehicular, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Flota Vehicular"
        unique_together = ('placa', 'chasis')