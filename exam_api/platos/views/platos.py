# catalog/views/category.py
from rest_framework import viewsets, filters
from platos.models.platos import Platos
from platos.serializer.platos import PlatosSerializer

class PlatosViewSet(viewsets.ModelViewSet):
    queryset = Platos.objects.all()
    serializer_class = PlatosSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name","categoria","descripcion")
    ordering_fields = ("precio","tiempo_preparacion_min","calorias")
