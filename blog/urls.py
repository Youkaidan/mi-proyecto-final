from django.urls import path
from blog.views import index as blog_index                           
from blog.views import InsertJuego, InsertDesarrollador, InsertNoticias, BuscarJuego

#URLS DE PROYECTO FINAL

urlpatterns = [
    path('', blog_index), 
    path('juego_insert', InsertJuego.as_view()) ,
    path('desarrollador_insert', InsertDesarrollador.as_view()) ,
    path('noticias_insert', InsertNoticias.as_view()) ,
    path('buscarj', BuscarJuego.as_view()),
]