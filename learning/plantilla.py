import tkinter as tk

"""
aun me falta ver el metodo trace y creo q es util para cuando 
actualizo el valor del contador editandolo de la caja de texto.

Cuando hago clic en el boton se imprime por consola, pero
cuando edito la caja no se imprime.

Por otra parte me falta controlar el tamaño de ventana.

"""
class Datos:
    def __init__(self):
        # Crea e inicializa una variable de control
        self.contador = tk.IntVar(value=0)

    # El metodo set permite modificar el valor de una variable de control
    def set_contador(self):
        self.contador.set(self.get_contador_valor() + 1)

    def get_contador(self):
        return self.contador

    # El metodo get permite obtener el valor de una variable de control
    def get_contador_valor(self):
        return self.get_contador().get()


class Formulario_Simple:
    def __init__(self, ventana):
        self.ventana = ventana

        # Estos son los Wigets del formulario
        # Con la propiedad textvariable de los widget asociamos las variables de control
        self.etiqueta = tk.Label(ventana, textvariable=valores.get_contador())
        self.caja_texto = tk.Entry(ventana, textvariable=valores.get_contador())
        self.boton = tk.Button(ventana, text="Actualizar Contador",
                               command=self.update_contador)

        self.dibujar()

    def dibujar(self):
        self.etiqueta.grid(row=1, column=1)
        self.caja_texto.grid(row=1, column=2)
        self.boton.grid(row=2, column=1)

    def update_contador(self):
        valores.set_contador()
        print(valores.get_contador_valor())


# Globales
gui = tk.Tk()
valores = Datos()

def init():
    if __name__ == '__main__':

        gui.title('Ventana Principal')
        gui.iconbitmap(default='favicon.ico')
        gui.geometry("300x300")
        #gui.config(width=800, height=800)

        formulario = Formulario_Simple(gui)

        gui.mainloop()

        #while True:
         #   root.update_idletasks()
          #  root.update()

init()
