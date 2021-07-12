from django.contrib import admin
from .models import Category, Article
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)# le coloco una coma aqui paro q lo interprete como una tupla
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at') # aparece user en el panel de adminitrador 
    search_fields = ('title', 'content', 'user__username', 'Categories__name')#user__username  es que me va a permitir buscar el nombre de usuario __ estamos accediendo a una propiedad que hay  con este modelo que esta relacionado con modelo articulo 
    list_display = ('title',  'user',  'public', 'created_at')
    list_filter = ('public', 'user__username', 'Categories__name')

    def save_model(self, request, obj, form, change): # estos son parametros nesesarios para poder crear este hook  objeto, formulario,change resquest y self
        if not obj.user_id: # si no me llega un usuario  o si no exite algo 
            obj.user_id = request.user.id # en caso de que no llege esta propiedad  obj.user le asigno un valor 
           # request.user.id le pasamos id de ese objeto usuario que me llega
        obj.save()        # y luego ya guardo  el objeto

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
