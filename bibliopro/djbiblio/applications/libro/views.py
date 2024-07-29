from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer


class Listaautores(ListAPIView):
   def get(self,request, *args,**kwargs):
       return self.list(request, *args, **kwargs)
   
   
   def get_queryset(self):
       queryset=Autor.objects.listar_autores_pais('Argentina')
       return queryset
   
class Filtroautores(ListAPIView):
   serializer_class = AutorSerializer
   
   def get_queryset(self):
       print ('******')
       edad=self.kwargs['edad']
       contry=self.kwargs['pais']
       print('---',contry, edad)
       queryset=Autor.objects.listar_autores_pais(contry)
       return queryset
   
class LibrosPosteriores(ListAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        year = self.kwargs['year']
        queryset=Libro.objects.lista_libros_posteriores(year)
        
        return queryset