from django.urls import path  
from . import views # el punto es el directorio actual de views

urlpatterns = [
    path('articulos/', views.list, name="list_articles"),
    path('categoria/<int:category_id>', views.category, name="category"),
    path('articulo/<int:article_id>', views.article, name="article")#le pasamos el nombre de la ruta y el prametro que va hacer un numero entero que seria article_id
]
