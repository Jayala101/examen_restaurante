from django.db import models

class Platos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=120, unique=True)
    descripcion = models.CharField(max_length=120)
    categoria = models.CharField(max_length=120, unique=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    tiempo_preparacion_min = models.IntegerField()
    calorias = models.IntegerField()
    es_vegetariano = models.BooleanField(default=False)
    nivel_picante = models.IntegerField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
    
    
