from django import forms
from blog.models import Juego, Desarrollador, Noticias

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class JuegoForm(forms.ModelForm):
  class Meta:
    model = Juego
    fields = ['nombre_juego', 'desarrollador', 'genero', 'cantidad_jugadores', 'resena']

class DesarrolladorForm(forms.ModelForm):
  class Meta:
    model = Desarrollador
    fields = ['nombre_desarrollador', 'pais', 'anno_fundacion']

class NoticiasForm(forms.ModelForm):
  class Meta:
    model = Noticias
    fields = ['titulo', 'sub_titulo', 'contenido', 'fecha']    
