"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # aqui importamos path y funcion include 
#  se comenta por el include y las  views que se encuentra en sus respectivas app from mainapp import views # importamos la carpeta mainapp  solo las vistas
# se comenta por el include  y las  views que se encuentra en sus respectivas app import pages.views # page es una app agregada se coloca el as page_views o  import page.views porque la confunde la views y daria error si la colocamos igual que arriba
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),  # '' se deja vacio la primera ruta porque quiero que esa ruta no tenga ningun nivel esta la ruta de una app en concreta
    path('', include('pages.urls')),  
    path('', include('blog.urls'))  
]
 #Ruta imagenes
if settings.DEBUG: # que compruebe el proyecto esta en modo debug para poder cargar aqui nuestra imagenes en el servidor local 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
    
    

