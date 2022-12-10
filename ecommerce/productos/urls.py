from django.urls import path
from productos.views import *

urlpatterns = [
    path("inicio/", inicio, name="productos-inicio"),
    #path("admin/inicio/", admin_inicio, name="admin-inicio"),
    path("nuevo_deporte/",deportes_nuevo,name="deportes-nuevo"),
    path("nuevo_articulo/",articulo_nuevo,name="articulo-nuevo"),
    path("articulos_listar/",articulos_listar,name="articulos-listar")
]