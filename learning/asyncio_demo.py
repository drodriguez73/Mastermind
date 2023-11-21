import sys
import tkinter as tk
from tkinter import ttk
import asyncio

"""
Aprendi Canvas desde estos links
    1. http://acodigo.blogspot.com/2017/03/tkinter-canvas.html
    2. https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=73&codigo=73&inicio=60
    3. https://stackoverflow.com/questions/47249451/tkinter-move-object-on-canvas

"""


class GameForm:
    def __init__(self, ventana, canvas, color):
        self.ventana  = ventana
        self.canvas = canvas
        self.pelota = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.x = 10
        self.y = 10

    def draw(self):
        self.canvas.move(self.pelota, self.x, self.y)
        self.x += 10
        self.y += 10

    def cerrar(self):
        self.ventana.destroy()
        app_.set_bucle(False)





class App:
    def __init__(self):
        self.bucle = True
        self.root = tk.Tk()
        self.root.title = "MainLoop Game"

        self.canvas = tk.Canvas(self.root, width=500, height=400, background="black")
        self.canvas.pack()

        self.game = GameForm(self.root, self.canvas, "red")

        self.root.protocol("WM_DELETE_WINDOW", self.game.cerrar)

    def set_bucle(self, flag):
        self.bucle = flag

    def get_bucle(self):
        return self.bucle

    async def game_gui(self):
        while self.bucle:
            self.game.draw()
            self.root.update_idletasks()
            self.root.update()

            await asyncio.sleep(3)


    async def arrancar(self):
        task1 = asyncio.create_task(self.game_gui())
        await task1

def main(argv):
    asyncio.run(app_.arrancar())


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

app_ = App()


init()