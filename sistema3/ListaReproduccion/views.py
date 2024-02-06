from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancion, Usuario

# Create your views here.

def inicio(request):
    lista_cancion =Cancion.objects.all()
    dicc ={"canciones":lista_cancion, "Saludo": "Bienvenido a su :"}
    return render(request, "index.html",dicc)

def login(request):
    return render(request, "login.html")

def autenticar(request):
    if request.method == 'POST' :
        usuario = request.POST['usuario'] 
        password = request.POST['password']

        if usuario in Usuario.objects.values_list('nickname', flat=True) and password in Usuario.objects.values_list('password', flat=True):
            usuario_autenticado = Usuario.objects.values('nickname', 'nombre_apellido', 'nickname').distinct().filter(nickname = usuario)
            lista_cancion = Cancion.objects.filter(usuario_id = usuario) 
            return render(request,"index.html",{'usuario':usuario_autenticado, 'canciones':lista_cancion})
        else: 
            return render(request, "login.html") 

    else:
        return HttpResponse("Que estas haciendo")


def agregar_cancion(request):
    if request.method == 'POST' :
        autor = request.POST['autor']
        titulo = request.POST['titulo']
        genero = request.POST['genero']
        