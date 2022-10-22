from unittest.util import _MAX_LENGTH
from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14, default='')
    construido_por = models.CharField(max_length=30, default='')
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')

class Juego(models.Model):
    nombre_juego = models.CharField(max_length=30, default='')
    desarrollador = models.CharField(max_length=30, default='')
    genero = models.CharField(max_length=30, default='')
    cantidad_jugadores = models.CharField(max_length=30, default='')
    resena = models.CharField(max_length=300, default='')

class Desarrollador(models.Model):
    nombre_desarrollador = models.CharField(max_length=30, default='')
    pais = models.CharField(max_length=30, default='')
    anno_fundacion = models.CharField(max_length=30, default='')

class Noticias(models.Model):
    titulo = models.CharField(max_length=60, default='')
    sub_titulo = models.CharField(max_length=60, default='')
    contenido = models.CharField(max_length=300, default='')
    fecha = models.CharField(max_length=20, default='')
