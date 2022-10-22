from ejemplo.models import Familiar
from blog.models import Configuracion, Juego, Desarrollador, Noticias

#Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
#Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
#Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
#Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
#Familiar(nombre="Erwin", direccion="Calle uno 222", numero_pasaporte=654321).save()

Configuracion(nombre_blog="Blog Gamer", construido_por="Erwin Orellana", titulo_principal="Reseñas de Videojuegos", subtitulo_principal="En éste blog encontraras reseñas y noticias de Videojuegos.").save()

Juego(nombre_juego="Cyberpunk 2077", 
desarrollador="CD Projekt Red", 
genero="Disparos/Rol", 
cantidad_jugadores="Un jugador", 
reseña="La historia sigue la lucha de V mientras lidia con un misterioso implante cibernético que amenaza con sobrescribir su cuerpo con la personalidad y los recuerdos de una celebridad fallecida que solo V percibe; los dos deben trabajar juntos si hay alguna esperanza de separarlos y salvar la vida de V.").save()

Desarrollador(nombre_desarrollador="CD Projekt Red", 
pais="Polonia", 
anno_fundacion="1995").save()

Noticias(titulo="CD Projekt Red festeja", 
sub_titulo="Cyberpunk 2077 llegó al millón de jugadores diarios en el último mes", 
contenido="El estudio polaco celebró el hito en redes sociales y le agradeció a todos los jugadores que le han brindado su apoyo.",
fecha="21/10/2022").save()


print("Se cargo con éxito la data base")