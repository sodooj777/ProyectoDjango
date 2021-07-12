from django.contrib import admin
from .models import Page # con el aterisco importamos todos mis modelos

# Configuracion extra 
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    search_fields = ('title', 'content') # este es un buscador en admin  
    list_filter = ('visible',) # un filtro 
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page , PageAdmin)


# Configuracion del panel
title = "Proyecto con Django"
subtitle = "Panel de gestion"

admin.site.site_header = title
admin.site.site_title = title # el titulo que aparece en la pestaña del navegador
admin.site.index_title = subtitle
