"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, index_tres, imc, 
                           monstrar_familiares, BuscarFamiliar, AltaFamiliar)
from blog.views import index as blog_index                           
from blog.views import InsertJuego, InsertDesarrollador, InsertNoticias, BuscarJuego

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    path('mostrar-notas/', index_tres), 
    path('imc/<peso>/<altura>/', imc), 
    path('mi-familia/', monstrar_familiares), 
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # clase 20 form
    path('mi-familia/alta', AltaFamiliar.as_view()), # clase 21

    path('blog/', blog_index), #URLS DE PROYECTO FINAL
    path('blog/juego_insert', InsertJuego.as_view()) ,
    path('blog/desarrollador_insert', InsertDesarrollador.as_view()) ,
    path('blog/noticias_insert', InsertNoticias.as_view()) ,
    path('blog/buscarj', BuscarJuego.as_view()),
    
]