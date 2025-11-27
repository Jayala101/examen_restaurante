# mesas/views/cuenta.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def calcular_cuenta_total(request):
    """
    Endpoint: POST /mesas/cuenta-total
    Calcula el total de una cuenta de mesa y categoriza según el monto.
    """
    try:
        # Obtener los precios del JSON de entrada
        precios = request.data.get('precios', [])
        
        # Validar que precios sea una lista
        if not isinstance(precios, list):
            return Response({
                'error': 'El campo precios debe ser una lista de números'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validar que todos los elementos sean números
        for precio in precios:
            if not isinstance(precio, (int, float)) or precio < 0:
                return Response({
                    'error': 'Todos los precios deben ser números positivos'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Calcular el total usando un ciclo
        total = 0
        for precio in precios:
            total += precio
        
        # Determinar el mensaje según el total
        if total < 20:
            mensaje = "Cuenta pequeña"
        elif 20 <= total <= 60:
            mensaje = "Cuenta media"
        else:  # total > 60
            mensaje = "Cuenta alta"
        
        return Response({
            'total': total,
            'mensaje': mensaje
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Error interno del servidor: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def aplicar_descuento(request):
    """
    Endpoint: POST /mesas/descuento
    Aplica un descuento porcentual a un total.
    """
    try:
        # Obtener datos del JSON de entrada
        total = request.data.get('total')
        porcentaje = request.data.get('porcentaje')
        
        # Validar que los campos estén presentes
        if total is None or porcentaje is None:
            return Response({
                'error': 'Los campos total y porcentaje son requeridos'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validar que sean números
        if not isinstance(total, (int, float)) or not isinstance(porcentaje, (int, float)):
            return Response({
                'error': 'Total y porcentaje deben ser números'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validar que el total sea positivo
        if total < 0:
            return Response({
                'error': 'El total debe ser un número positivo'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validar el porcentaje con condicionales
        if porcentaje < 0 or porcentaje > 100:
            return Response({
                'error': 'El porcentaje debe estar entre 0 y 100'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Calcular descuento
        monto_descuento = total * (porcentaje / 100)
        total_con_descuento = total - monto_descuento
        
        return Response({
            'total': total,
            'porcentaje': porcentaje,
            'monto_descuento': monto_descuento,
            'total_con_descuento': total_con_descuento
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': f'Error interno del servidor: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def horas_estudio(request):
    try:
        horas = request.data.get('tiempo_preparacion_min',[])
        promedio = request.data.get('precio')
    
        if horas is None:
            return Response({
                'error':'el campo de horas de estudio es obligatorio'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    
        promedio = 0
        for hora in horas:
            promedio += hora
            
        promedio = promedio / 7
        
        if promedio < 1:
            message = "Estás estudiando muy poco"
        if 1 <= promedio <= 3:
            message = "Buen ritmo de estudio"
        else:
            message = "Excelente dedicación"
        
        return Response({
            'horas': horas,
            'message': message
        }, status=status.HTTP_200_OK)
        
        
    except Exception as e:
        return Response ({
            'error': f'Error internal server error {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERRROR)
        
@api_view(['POST'])
def promedio_estudio(request):
    try:
        notas = request.data.get('tiempo_preparacion_min',[])
        promedio = request.data.get('precio')
    
        if notas is None:
            return Response({
                'error':'el campo de horas de estudio es obligatorio'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    
        promedio = 0
        
        for nota in notas:
            promedio += nota
            
        res = promedio / len(notas)
        
        if res < 7:
            message = "Reprobado"
        else:
            message = "Aprobado"
        
        return Response({
            'notas': notas,
            'message': message
        }, status=status.HTTP_200_OK)
        
        
    except Exception as e:
        return Response ({
            'error': f'Error internal server error {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERRROR)