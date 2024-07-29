from django.urls import path, register_converter
from . import views, converters


app_name = "libro_app"

class TwoDigitNumber:
     regex='[0-9]+'
     
     def to_python(self, value):
          number=int(value)
          if number>15:
               return number
          else:
               raise ValueError('error de numero')
          
        
     def to_url(self, value):
          return value

register_converter(TwoDigitNumber,'nn')
register_converter(converters.ValidYearsConvert,'aaaa')

urlpatterns = [
     path('api/autor/list', views.Listaautores.as_view()),
    # path('api/autor/filtro/<int:pais>/', views.Filtroautores.as_view()),
     path('api/autor/filtro/<nn:edad>/<pais>/', views.Filtroautores.as_view()),
     path('api/libro/posteriores/<aaaa:year>/', views.LibrosPosteriores.as_view()),
]