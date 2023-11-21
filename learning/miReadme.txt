# Introducción a TKinter (Tcl/Tk)

Tk es una biblioteca de código abierto escrita en C y desarrollada en sus orígenes para el lenguaje de programación Tcl, de ahí que usualmente nos refiramos a ella como [Tcl/Tk](https://docs.python.org/3/library/tkinter.html). Desde sus primeras versiones Python incluye en su biblioteca o librería estándar el módulo tkinter, que permite interactuar con Tk para desarrollar aplicaciones de escritorio en Python.


### Un template tipico de una app en tkinter es

El siguiente codigo esta muy bien explicado en [Recursos Python](https://recursospython.com/guias-y-manuales/introduccion-a-tkinter/) donde ademas hay una importante colección de artículos y códigos de fuentes.

```
ver ventana_simple.py
ver plantilla.py
```


### Widget & Variables de control

La siguiente lista son [variables de control](https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html), objetos especiales que se asocian a los widgets para almacenar sus valores y facilitar su disponibilidad en otras partes del programa. 

Cuando una variable de control cambia de valor el widget que la utiliza lo refleja automáticamente, y viceversa.

Todas la variables de control deben estar asociadas a una ventana. Por ejemplo suponiendo q tenemos el siguiente codigo

`root = tk.Tk()`

la varible de control la creamos explicitamente asi

`contador = tk.IntVar(root, value=0)`

o asi

`contador = tk.IntVar(value=0)`

- IntVar()
- DoubleVar()
- StringVar()
- BooleanVar()
- Label()
- Entry()


## Las distintas librerias tk, ttk y tix

https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html

# Posicionamiento

Como en todas las ventanas graficas tenemos varias formas de ubicar los widgets dentro de la pantalla

- grid
- cordenadas x, y
- pack()



## Tablas y dataframe

La forma mas simple de mostrar datos en formato de tabla es utilizando la funcionalidad propia de los dataframes de pandas y mostrarlo en un [widget de texto](https://es.stackoverflow.com/questions/340278/como-mostrar-un-dataframe-en-tkinter) en tkinter. 

Pero esto tiene una funcionalidad muy basica, si pensamos en agregar mas funcionalidad como:

- add, remove rows and columns
- spreadsheet-like drag, shift-click, ctrl-click selection
- edit individual cells
- sort by column, rename columns
- reorder columns dynamically by mouse drags
- set some basic formatting such as font, text size and column width
- save the DataFrame to supported pandas formats
- import/export of supported text files
- rendering of very large tables is only memory limited
- interactive plots with matplotlib, mostly using the pandas plot functions
- basic table manipulations like aggregate and pivot
- filter table using built in dataframe functionality
- graphical way to perform split-apply-combine operations

entonces [pandasTable](https://pandastable.readthedocs.io/en/latest/description.html) es la opcion. Para mostrar la tabla por pantalla es conveniente meterla dentro de un [frame](https://enriquelazcorreta.gitbooks.io/tkinter/content/creando-la-interfaz-grafica-de-usuario-gui/frame.html) de tal forma de poder controlarla particularmente ademas de [ubicarla](https://unipython.com/tkinter-widgets-frame-y-metodo-pack/) dentro de la ventana principal en un lugar adecuado.




## El metofo mainloop() y los bloqueos

Es el bucle principal del programa. Todas las aplicaciones de escritorio trabajan con un bucle principal que se ocupa de gestionar los eventos de la interfaz gráfica. El bucle principal se está ejecutando constantemente y una de sus tareas principales es dibujar y gestionar los eventos en la pantalla.

El [bucle se ejecuta infinitamente](https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop) hasta que cerremos la ventana principal, recien ahi se ejecutara el resto del codigo de la app.

Por lo general la forma mas simple de ejecutar el bucle es

`tk.mainloop()`


Para la mayoria de la app el metodo mainloop() es perfecto, pero cuando trabajamos con aplicaciones que requieran de tareas concurrentes, al ser este un metodo bloqueante no nos sirve. El caso mas comun es mostras datos en tiempo real que recibimos por websockets.

Una alternativa para evitar el codigo bloqueante del mainloop es escribirlo asi

```
while True:
    tk.update_idletasks()
    tk.update()

```


## Mainloop, asyncio y websockets

Excelente intro para utilizar asyncio con tkinter para majejar el mecanismo de [loops con async](https://www.loekvandenouweland.com/content/python-asyncio-and-tkinter.html)

Tambien podemos leer este articulo de un novato como yo haciendo su [primera experiencia](https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui)

Running asyncio loop and tkinter gui
https://stackoverflow.com/questions/68510708/running-asyncio-loop-and-tkinter-gui


## Caracteristicas de la Gui

How to set Tkinter Window Size?

`gui.geometry("600x600")`


# Mastermind 

is a [Gui](https://github.com/prestonkelly/Mastermind) for buying, selling and analyzing cryptocurrency.
	
		