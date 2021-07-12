from django.db import models
from ckeditor.fields import RichTextField #tenemos que importar el Richtextfield porque sino django no sabe lo que esta buscando y daria error es un tipo de campo que esta en dentro de la app de ckeditor  y fields para poder importas esos ficheros
# y una ves instalada la app de ckeiditor si la vamos utilizar agregar en settings.py  INSTALED_APP 

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido") # le colocamos RichText field para que se un editor de texto enriquesido y no tenemos que acceder desde models. 
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")#slug es para hacer una url amigable  para luego implementar eso # unique = True le estamos diciendo que el campo charfield sea unico 
    order = models.IntegerField(default=0,verbose_name="Orden") #  en el caso que sea  0 me lo va a poner al principio de todo en esa pagina
    visible = models.BooleanField(verbose_name="Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at =  models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name ="Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title