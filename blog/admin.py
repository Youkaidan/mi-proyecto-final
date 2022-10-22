from django.contrib import admin
from blog.models import Configuracion, Juego, Desarrollador, Noticias

admin.site.register(Configuracion)
admin.site.register(Juego)
admin.site.register(Desarrollador)
admin.site.register(Noticias)
