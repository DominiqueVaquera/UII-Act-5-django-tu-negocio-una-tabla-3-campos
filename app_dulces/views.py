from django.shortcuts import render
from .models import Dulce

def index(request):
    # 1. Obtener todos los objetos Dulce
    dulces = Dulce.objects.all()
    
    # 2. Crear el diccionario de contexto.
    # Es importante que la clave 'Dulces' coincida con la usada en tu plantilla HTML.
    contexto = {'Dulces': dulces}

    # 3. Renderizar la plantilla 'index.html' con el contexto.
    # Solo se devuelve el resultado de la función render.
    return render(request, 'index.html', contexto)