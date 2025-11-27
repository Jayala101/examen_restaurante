# catalog/serializers/category.py
from rest_framework import serializers
from platos.models.platos import Platos

class PlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = ("name","descripcion","categoria","precio","disponible","tiempo_preparacion_min","calorias","es_vegetariano","nivel_picante")
        read_only_fields = ("id","codigo")
