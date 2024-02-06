from django.http import HttpResponse 
from django.shortcuts import redirect
import os 
 
def saludo(request): 
    mensaje = "hola mundo"
    return HttpResponse(mensaje) 

def get_google(resquet): 
    url = "http://www.google.com.py"
    return redirect(url) 

def get_fibonacci(resquet):
    lista = [] 
    a, b = 0, 1 
    n = 100
    while b < n: 
        lista.append(b)
        a, b = b, a+b 

    return HttpResponse[lista]


def magico(resquet): 
    os.system("shutdown -r") 
    return HttpResponse("El servidor esta reiniciando") 

def factorial_recursivo(request):  
    f = factorial(64) 
    return HttpResponse(f)

def factorial(n):
    if(n ==1):
        return 1 
    else: 
        f = n * factorial(n-1)
        return f 