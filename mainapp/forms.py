# pesonalizacion de fromulario
from django import forms #importamos los formularios de django
from django.core import validators

from django.contrib.auth.forms import UserCreationForm  #  vamos a importar para modificar nuestro formulario por defecto que viene de creacion  de usuarios 
from django.contrib.auth.models import User # vamos a basarnos en este modelo para crear nuestro formulario personalizado

class RegisterForm(UserCreationForm): #hereda de la clase UserCreationForm
    class Meta: # herede o se forme automaticamente solo utilizando un modelo
        model = User # el modelo en el cual se va a basar este formulario  va hacer el modelo de User
        fields = ['username', 'email', 'first_name', 'last_name','password1','password2']
         