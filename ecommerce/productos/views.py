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

def articulo_nuevo(request):
    #acá me traigo los datos desde el formulario y los guardo en variables para luego crear la instancia
    if request.method == "POST":
        deporte_nuevo = request.POST["deporte"]
        nombre_nuevo = request.POST["nombre"]
        marca_nuevo = request.POST["marca"]
        descripcion_nuevo = request.POST["descripcion"]
        precio_nuevo = request.POST["precio"]
        publicacion_nuevo = request.POST["publicacion"]
        imagen_nuevo = request.FILES["imagen"]

        deporte_instancia = Deporte.objects.filter(nombre=deporte_nuevo)[0]
        marca_instancia = Marca.objects.filter(nombre=marca_nuevo)[0]

        #creo una instancia llamada "persona_nueva" de la clase "Persona" con los atributos que traigo desde el formulario
        articulo_nuevo = Articulo(deporte=deporte_instancia, nombre=nombre_nuevo,marca=marca_instancia, descripcion=descripcion_nuevo, precio=precio_nuevo, publicacion=publicacion_nuevo, imagen=imagen_nuevo)
        articulo_nuevo.save() #con esto lo guardo en la base de datos
        return redirect("productos-inicio")

    marcas = Marca.objects.all()
    deportes = Deporte.objects.all()
    return render(request, "productos/articulo_nuevo.html",{"marcas":marcas,"deportes":deportes})