from django.shortcuts import render, get_object_or_404 #esto lo que hace el get_object_or_404 
from django.core.paginator import Paginator # el Paginator simplemente es un objeto que nos permite hacer la paginacion de forma sencilla
from blog.models import Category, Article # importamos el modelo de mi app blog Category y Article
from django.contrib.auth.decorators import login_required #importamos decoradores de la autennticacion 
# si y importo el login_required le puedo decir a una ruta que yo tenga aqui suelta 

# Create your views here.
# le aplicamos el decorador @login_required se tiene que colocar tal cual asi eso restrige el acceso a las paginas web
@login_required(login_url="login")# aqui (le digo a donde quiero que me lleve en caso de que yo entre a esta pagina o 
# esta ruta que tiene un decorador de login_require es requerido identificarse para poder entrar a esta pagina)
# login_url simplemente es la ruta login
def list(request):
    
    # sacar articulos
    articles = Article.objects.all()# vamos hacer una consulta  a la base de datos 
    
    # paginar los articulos
    paginator = Paginator(articles, 2)#le pasamos la lista de articulos que queremos paginar  solo dos elementos le colocamos el numero de elemento que queremos por pagina
    
    #recoger  numero pagina
    page = request.GET.get('page')# request.GET para recoger un parametro get de la url  y voy a conseguir el parametro page
    
    page_articles = paginator.get_page(page) # page_articles aqui se guarda todos lo articulos de esa pagina
    # paginator es la paginacion como tal get_page y le paso el numero de la pagina en este caso (page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })
@login_required(login_url="login")
def category(request, category_id):

    category =  get_object_or_404(Category, id=category_id) #en el caso de  no exitir una pagina de categoria http://localhost:8000/articulos/5664 y me va mostrar una pagina 404  
   # articles = Article.objects.filter(Categories=category)#esto es lo mismo q lo que esta despues de with en category.html

    return render(request, 'categories/category.html', {
        'category': category,
        #'articles': articles 
    })
@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',   {
        'article': article
    })