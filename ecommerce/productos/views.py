from django.shortcuts import render
from productos.models import *
from django.contrib.auth.decorators import login_required
from usuarios.views import avatar_usuario


def inicio(request):
    return render(request,"productos/inicio.html",{"avatar":avatar_usuario(request.user)})

# Función para listar todos los artículos
@login_required
def articulos_listar(request):
    #obtengo el listado de articulos de la base de datos
    lista_articulos = Articulo.objects.all()
    contexto = {"articulos_resultado":lista_articulos}

    return render(request,"productos/articulos_listar.html", contexto)