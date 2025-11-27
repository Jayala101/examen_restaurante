# mesas/urls.py
from django.urls import path
from mesas.views.cuenta import calcular_cuenta_total, aplicar_descuento,horas_estudio,promedio_estudio

urlpatterns = [
    path('cuenta-total', calcular_cuenta_total, name='calcular_cuenta_total'),
    path('descuento', aplicar_descuento, name='aplicar_descuento'),
    path('total-horas',horas_estudio, name='horas_estudio'),
    path('promedio-estudio',promedio_estudio, name='promedi-estudio'), 
]
