from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .serializers import PrestamoSerializer
from .models import Prestamo



class ListarPrestamos(ListAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        lista= Prestamo.objects.listar_prestamo_fecha('2024-07-22')
        return lista
    
    
    
