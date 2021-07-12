from django.shortcuts import render
from .models import Page  #directorio actual y fichero models
from django.contrib.auth.decorators import login_required  #importamos decoradores de la autennticacion 
# si y importo el login_required le puedo decir a una ruta que yo tenga aqui suelta por ejemplo a la page

# Create your views here.
# le aplicamos el decorador @login_required se tiene que colocar tal cual asi

@login_required(login_url="login") # aqui (le digo a donde quiero que me lleve en caso de que yo entre a esta pagina o 
# esta ruta que tiene un decorador de login_require es requerido identificarse para poder entrar a esta pagina)
# login_url simplemente es la ruta login
def page(request, slug): # request va a recibir todos los datos de la peticion le pasamos el slug como segundo parametro
    # creamos una variable que se llame page  y dentro  de la variable le asignamos un valor Page.objects.get y esto me va hacer una consulta un select * from a la tabla de la base de datos
    page = Page.objects.get(slug=slug)    # simplemente este seria el campo de la base de datos slug=  y este seria el valor que me llega como parametro que me llega de la url slug
     
    return render(request, "pages/page.html", { # aqui vamos a cargar  la pagina que esta dentro de la carpeta pages
        "page": page
    })