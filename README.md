## mi-proyecto-final 

# Entrega Proyecto Final

- Antes de realizar las pruebas cargar datos iniciales en el modelo, uliziando el archivo seed_data.py

```bash
python manage.py shell < seed_data.py
```

- Las 3 clases existentes en el modelo, sobre las cuales operan las funcionalidades son: Juego, Desarrollador y Noticias

# Pantalla base - Index

- Ejecutar ```python manage.py runserver``` e ir a [http://127.0.0.1:8000/blog](http://127.0.0.1:8000/blog)

- Lá pagina principal contiene las siguientes funcionalidades

![index](/entrega_final.png)

- Encabezado, pie de pagina y menú izquierdo son heredados por el resto de las vistas
- Menú de Usuario y Menú de Contenido muestran distintas opciones según autenticación.

# Insertar / Modificar datos

- En el costado inferior izquierdo, en la seccion de ```Menú contenido```, una vez autenticado, podrá observar funciones CRUD.
- En la nueva vista, complete el formulario y haga click en el botón Ingresar.
- A continuación puede repetir el procedimiento seleccionando otro link en el cuadro ```Menú contenido``` o hacer click en ```Blog Gamer``` / ```Home``` para regresar al index.

![index](/insertar_noticia.png)

# Buscar datos - Juego / Noticias

- En el costado izquierado, en la seccion de ```Buscar Noticia / Buscar Juego```, ingrese el string a buscar y presione ```Buscar!```
- En la nueva vista, podra observar los resultados del objeto buscado.
- A continuación puede repetir el procedimiento ingresando una nueva busqueda en ```Buscar``` o hacer click en ```Blog Gamer``` / ```Home``` para regresar al index.

![index](/buscar_juego.png)

# VIDEO FUNCIONALIDADES

[![Alt text](https://img.youtube.com/vi/VSv0oUKahfM/0.jpg)](https://www.youtube.com/watch?v=VSv0oUKahfM)

***Desarrollado por: Erwin Orellana.-***
***Noviembre/2022***
