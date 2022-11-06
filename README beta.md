## mi-proyecto-final 

# Entrega Intermedia del Proyecto Final

- Antes de realizar las pruebas cargar datos iniciales en el modelo, uliziando el archivo seed_data.py

```bash
python manage.py shell < seed_data.py
```

- Las 3 clases existentes en el modelo, sobre las cuales operan las funcionalidades son: Juego, Desarrollador y Noticias

# Set de pruebas - Index

- Ejecutar ```python manage.py runserver``` e ir a [http://127.0.0.1:8000/blog](http://127.0.0.1:8000/blog)

- Lá pagina principal contiene las siguientes funcionalidades

![index](/primera_entrega.png)

- Encabezado, pie de pagina y menú izquierdo son heredados por el resto de las vistas

# Insertar datos

- En el costado inferior izquierdo, en la seccion de ```insertar contenido```, seleccione uno de los 3 modelos.
- En la nueva vista, complete el formulario y haga click en el botón Ingresar.
- A continuación puede repetir el procedimiento seleccionando otro link en el cuadro ```Insertar contenido``` o hacer click en ```Blog Gamer``` / ```Home``` para regresar al index.

# Buscar datos - Juego

- En el costado izquierado, en la seccion de ```Buscar Juego```, ingrese el string a buscar y presione ```Buscar!```
- En la nueva vista, podra observar los resultados del juego buscado.
- A continuación puede repetir el procedimiento ingresando una nueva busqueda en ```Buscar Juego``` o hacer click en ```Blog Gamer``` / ```Home``` para regresar al index.

***Desarrollado por: Erwin Orellana.-***
