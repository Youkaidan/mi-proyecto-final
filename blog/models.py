from unittest.util import _MAX_LENGTH
from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')

class Juego(models.Model):
    nombre_juego = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=30)
    genero = models.CharField(max_length=30, default='')
    cantidad_jugadores = models.CharField(max_length=30, default='')
    reseña = models.CharField(max_length=100, default='')

class Desarrollador(models.Model):
    nombre_desarrollador = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    anno_fundacion = models.CharField(max_length=30, default='')

class Noticias(models.Model):
    titulo = models.CharField(max_length=60)
    sub_titulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=200)
