from ejemplo.models import Familiar
from blog.models import Configuracion, Juego, Desarrollador, Noticias

#Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
#Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
#Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
#Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
#Familiar(nombre="Erwin", direccion="Calle uno 222", numero_pasaporte=654321).save()

Configuracion(nombre_blog="Blog Gamer", construido_por="Erwin Orellana", titulo_principal="Reseñas de Videojuegos", subtitulo_principal="En éste blog encontraras reseñas y noticias de Videojuegos.").save()

print("Se cargo con éxito la data base")