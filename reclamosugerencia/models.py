from django.db import models
from dependencias.models import Circuito, Subcircuito

# Create your models here.
class ReclamoSugerencia(models.Model):
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    subcircuito = models.ForeignKey(Subcircuito, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    detalle = models.CharField(max_length=200)
    contacto = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.detalle)
    
    def save(self):
        self.detalle = self.detalle.upper()
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(ReclamoSugerencia, self).save()

    class Meta:
        verbose_name_plural = "Reclamos y Sugerencias"
