from django.db import models
from ckeditor.fields  import RichTextField#tenemos que importar el Richtextfield porque sino django no sabe lo que esta buscando y daria error es un tipo de campo que esta en dentro de la app de ckeditor  y fields para poder importas esos ficheros
# y una ves instalada la app de ckeiditor si la vamos utilizar agregar en settings.py  INSTALED_APP 
from django.contrib.auth.models import User #auth es la app que tiene todo el tema de la autenticacion el registro de usario y todo eso . models y asi accedo a sus modelos
# from django.contrib.auth.models import User voy usar este modelo para hacer una clave agena
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at =  models.DateTimeField(auto_now_add=True, verbose_name="Creado el")


    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null",verbose_name="Imagen",upload_to="articles")#upload_to aqui le vamos a indicar en q carpeta queremos q se cargen las imagenes
    public = models.BooleanField(verbose_name="Publicado?")
    user = models.ForeignKey(User,editable=False, verbose_name="Usuario", on_delete=models.CASCADE)   #y esta campo llamado user se va relacionar con este otro modelo con la clave agena user # esto lo que va a guardar en la base de datos dentro de la propiedad de user va guardar el id del usuario que ha creado el articulo 
    # on_delete le vamos a indicar que cuando borre este articulo quiero que sea on_delete cascade QUE HACE EL ON_DELETE CACADE QUE SI YO BORRO EL REGISTRO CON EL CUAL ESTA RELACIONADO TAMBIEN SE BORRA EL OBJETO EL REGISTRO CON EL CUAL ESTA VINCULADO DE FORMA DE QUE SI YO BORRO UN USUARIO TODOS LOS ARTICULOS SE VAN A BORRA PORQUE TIENE EL ON_DELETE CASCADE
    # user me va a guardar el id del usuario luego va a meter una clave foranea y cuando yo saque un objeto articulo 
    # voy a tener disponible dentro de esta propiedad  un objeto completo de lo que viene el modelo de usuario
    # con todos los datos que eso tiene  es decir yo saco un articulo y a la vez voy a tener propiedades  q
    # que me saque el usuario las categoria donde pertenece  todo totalmente vinculado y relacionado   
    Categories = models.ManyToManyField(Category, verbose_name="Categorias",  blank=True)#ManyToMany este campo es que muchos articulos pueden tener multiples categoria  no es un articulo en concreto que puede tener muchas categorias cualquiera de los articulos puede tener muchas categorias
    # relacionamos con el modelo de category  que hace esto al final guardame la base de datos la relaciones que hay entre un articulo y una categoria seguramente creara una tabla picote  con esa informacion relacionando un id con otro id y asi 
    # blank es me da igual que el campo no tenga nada es decir que por defecto no estemos obligados a introducir ningun tipo de categoria  null me da igual que el campo este vacio o no
    # en el campo user editable = False sirve para no modificar un articulo de otro usuario si no solo el nuestro
    created_at =  models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at =  models.DateTimeField(auto_now=True, verbose_name="Editado el")
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at'] # lo ordena del la fecha mas nuevo al fechas mas viejo se coloca el - para que el orden sea descendente
    
    def __str__(self):
        return self.title