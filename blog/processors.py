# este es el mismo archivo que context processors  solo de blog
from blog.models import * # importamos todo modelo 

def get_categories(request):
    #colocamos una condicion con el metodo filters si esta condicion se cumple muestra todo lo visible  y me sigue mostrando mi values_list con una condicion preevia si esta como no visible no lo muestra
    # le colocamos order_by para ordenar desde el campo order del modelo de la base de datos
    ids = Article.objects.filter(public=True).values_list('Categories', flat=True) # flat =True en formato plano de esta forma vamos a tener todos los id  de la categorias  q esta siendo usadas
    categories = Category.objects.filter(id__in=ids).values_list('id', 'name')#Page importamos y llamamos la clase del modelo con el objeto con el value list podemos selecionar unos de los elementos que yo quiera o un par de elementos que quiero tener disponibles  por ejemplo quiero tener el id
    #id__in=ids puedo sacar las categorias cuyo id  se este usando en el listado de Categories en uso

    return {
        'categories': categories,
        'ids': ids 
    } 

