from pages.models import Page# importamos mi modelo de pagina

def get_pages(request):
    #colocamos una condicion con el metodo filters si esta condicion se cumple muestra todo lo visible  y me sigue mostrando mi values_list con una condicion preevia si esta como no visible no lo muestra
    # le colocamos order_by para ordenar desde el campo order del modelo de la base de datos
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')#Page importamos y llamamos la clase del modelo con el objeto con el value list podemos selecionar unos de los elementos que yo quiera o un par de elementos que quiero tener disponibles  por ejemplo quiero tener el id
    

    return {
        'pages': pages 
    } 
