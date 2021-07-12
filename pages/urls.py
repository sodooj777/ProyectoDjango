from django.urls import path  
from . import views  # el punto es el directorio actual de views

urlpatterns = [
     path('pagina/<str:slug>', views.page, name="page")  #/pagina/sobre-nosotros  le pasamos un parametro a la url que es el slug
]
