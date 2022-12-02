from django.shortcuts import render
from productos.models import *
from django.contrib.auth.decorators import login_required


# Función para listar todos los artículos
@login_required
def articulos_listar(request):
    #obtengo el listado de articulos de la base de datos
    lista_articulos = Articulo.objects.all()
    contexto = {"articulos_resultado":lista_articulos}

    return render(request,"productos/articulos_listar.html", contexto)