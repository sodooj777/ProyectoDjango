from django.shortcuts import render, redirect
from django.contrib import messages   # nucleo de framewor django.contrib importamos messages flas
from django.contrib.auth.forms import UserCreationForm # importamos un formulario que ya viene por defecto dentro de django y de esta manera vamos a tener un formulario totalmente funcional para registrar un usuario
from mainapp.forms import RegisterForm # cargamos el formulario personalizado
from django.contrib.auth import authenticate, login, logout  # modulo de autenticacion
from django.contrib.auth.decorators import login_required #importamos decoradores de la autennticacion 
# si y importo el login_required le puedo decir a una ruta que yo tenga aqui suelta  

# Create your views here.
def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio' # le pasamos el titulo del a pagina  
    })

def about(request):

    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros' # le pasamos el titulo del a pagina  
    })    

def register_page(request):
    
    if request.user.is_authenticated: #comprobamos en el caso de que el usuario si este autenticado 
        return redirect('index') # que me redirija a inicio 
    else:     # y en el caso de que no entoces si quiero que me muetres el otro formulario y me hagas el otro return
        register_form = RegisterForm()

        if request.method == 'POST':# voy a comprobar si me llega el metodo post  
            register_form = RegisterForm(request.POST)# le voy a pasar los datospost del formulario que yo he enviado en caso de que no me guarde nada que lo rellene automaticamente
            
            if register_form.is_valid(): #en el caso de que el formulario sea valido
                register_form.save() # y ese formulario automaticamente ya me registra un usuario porque es un formulario vinculado a ese tipo de modelo
                messages.success(request, 'Te has registrado correctamente!!') 

                return redirect('index') #en el caso que todo vaya bien quiero que me lleve al inicio 

        return render(request, 'users/register.html', {
            'title':'Registro',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated: #comprobamos en el caso de que el usuario si este autenticado 
        return redirect('index') # que me redirija a inicio 
    else:     # y en el caso de que no entoces si quiero que me muetres el otro formulario y me hagas el otro return
        if request.method == 'POST': # voy a comprobar si me llega el metodo post
            username = request.POST.get('username') # recogemos el dato que me llega de username 
            password = request.POST.get('password') # recogemos el dato que me llega de password

            user = authenticate(request, username=username, password=password) #le pasamos las crendenciales el kewor argumes de esta forma me voy a autenticar si la autenticacion es correcta
            # estes es el operador si no is not
            if user is not None: #en caso de que esto sea diferente a none en caso de que no sea none el usuario que sea correcto
                login(request, user) #vamos usar el metodo login y esto ya me va a crea la ssession de usuario etc le pasamos la request y el objeto usuario que quiere identificar 
                return redirect ('index') # y por ultimo hacemos una redireccion al inicio
            
            else: # en el caso de que la autenticasion haya fallado 
                messages.warning(request, 'No te has Identificado correctamente :(') #hacemos un message warning flas 


        return render(request, 'users/login.html', {
            'title':'Identificate'
        })

def logout_user(request):
    logout(request)# llamamos el metodo logout que tenemos importado arriba del sistema de autenticacion de django
    return redirect('login')   # quiero que me lleve al login

