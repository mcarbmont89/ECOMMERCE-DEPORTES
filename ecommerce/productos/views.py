from django.shortcuts import render,redirect
from productos.models import *
from django.contrib.auth.decorators import login_required
from usuarios.views import avatar_usuario


def inicio(request):
    deportes = Deporte.objects.all()
    contexto = {"avatar":avatar_usuario(request.user),"deporte_lista":deportes}
    return render(request,"productos/inicio.html",contexto)

# Función para listar todos los artículos
@login_required
def articulos_listar(request):
    #obtengo el listado de articulos de la base de datos
    lista_articulos = Articulo.objects.all()
    contexto = {"avatar":avatar_usuario(request.user),"articulos_resultado":lista_articulos}

    return render(request,"productos/articulos_listar.html", contexto)

def deportes_nuevo(request):
    #acá me traigo los datos desde el formulario y los guardo en variables para luego crear la instancia
    if request.method == "POST":
        nombre_nuevo = request.POST["nombre"]
        imagen_nuevo = request.FILES["imagen"]
                
        #creo una instancia llamada "persona_nueva" de la clase "Persona" con los atributos que traigo desde el formulario
        deportes_nuevo = Deporte(nombre=nombre_nuevo, imagen=imagen_nuevo)
        deportes_nuevo.save() #con esto lo guardo en la base de datos
        return redirect("productos-inicio")
        
    return render(request, "productos/deportes_nuevo.html")