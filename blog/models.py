from unittest.util import _MAX_LENGTH
from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14, default='')
    construido_por = models.CharField(max_length=30, default='')
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')

class Juego(models.Model):
    nombre_juego = models.CharField(max_length=50, default='')
    desarrollador = models.CharField(max_length=50, default='')
    genero = models.CharField(max_length=50, default='')
    cantidad_jugadores = models.CharField(max_length=30, default='')
    resena = models.TextField(max_length=3000, default='')

class Desarrollador(models.Model):
    nombre_desarrollador = models.CharField(max_length=50, default='')
    pais = models.CharField(max_length=30, default='')
    anno_fundacion = models.CharField(max_length=30, default='')

class Noticias(models.Model):
    titulo = models.CharField(max_length=100, default='')
    sub_titulo = models.CharField(max_length=255, default='')
    contenido = models.TextField(max_length=3000, default='')
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="noticias", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.titulo}"
