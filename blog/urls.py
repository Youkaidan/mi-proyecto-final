from django.urls import path
from blog.views import index as blog_index                           
from blog.views import InsertJuego, InsertDesarrollador, BuscarJuego
from blog.views import *

#URLS DE PROYECTO FINAL

urlpatterns = [
    path('', blog_index), 
    path('juego_insert', InsertJuego.as_view()) ,
    path('desarrollador_insert', InsertDesarrollador.as_view()) ,
    path('buscarj', BuscarJuego.as_view()),

    path('list/', ListNoticia.as_view(), name="list-noticia"),
    path('create/', CreateNoticia.as_view(), name="create-noticia"),
    path('detail/<int:pk>/', DetailNoticia.as_view(), name="detail-noticia"),
    path('update/<int:pk>/', UpdateNoticia.as_view(), name="update-noticia"),
    path('delete/<int:pk>', DeleteNoticia.as_view(), name="delete-noticia"),
    path('search-by-name-/', SearchNoticiaByName.as_view(), name="search-by-name-noticia"),
]