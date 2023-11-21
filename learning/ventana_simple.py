import tkinter as tk
import pandas as pd



class Ejemplo_RadioButton:
    # Raidiobutton
    # Lo basico
    # https://stackoverflow.com/questions/42845090/give-a-radio-button-a-default-value-in-tkinter-python
    # https://python-course.eu/tkinter/radio-buttons-in-tkinter.php
    # https://programacionfacil.org/blog/los-radiobutton-y-las-variables-de-control-de-tkinter/

    def __init__(self, ventana):
        self.ventana = ventana
        self.valor = tk.StringVar(None, 'B')
        self.titulos_radiobutton = None
        self.etiqueta_titulos = None

        self.dibujar_radio()

    def dibujar_radio(self):
        self.titulos_radiobutton = tk.Radiobutton(
            self.ventana,
            text = 'Titulo Pesos',
            variable = self.valor,
            command=lambda: self.actualizar_titulos_label(self.valor.get()),
            value='A')
        self.titulos_radiobutton.grid(row=0, column=1)

        self.titulos_radiobutton = tk.Radiobutton(
            self.ventana,
            text='Titulos en D o C',
            variable = self.valor,
            command=lambda: self.actualizar_titulos_label(self.valor.get()),
            # command = actualizar_titulos_label,
            value='B')
        self.titulos_radiobutton.grid(row=1, column=1)

        self.etiqueta_titulos = tk.Label(text=self.valor.get())
        self.etiqueta_titulos.grid(row=3, column=1)

    def actualizar_titulos_label(self, t):
        self.etiqueta_titulos.config(text=t)


class Ejemplo_SpinBox:
    # SpinBox
    # Lo basico
    # https://recursospython.com/guias-y-manuales/caja-de-texto-numerica-spinbox-en-tkinter/


    def __init__(self, ventana):
        self.ventana = ventana

        self.txt_comision_tomadora = "Comision Tomdora:"

        self.label_comision_tomadora = tk.Label(text="")
        self.label_comision_colocadora = tk.Label(text="Comision Colocadora:")

        self.spin_tomadora = tk.DoubleVar(value=1.0)
        self.spin_colocadora = tk.DoubleVar(value=0.0)

        self.dibujar_spin()

    def dibujar_spin(self):

        #self.label_comision_tomadora.config(text=self.txt_comision_tomadora)
        self.label_comision_tomadora['text'] = self.txt_comision_tomadora

        self.label_comision_tomadora.grid(row=1, column=1)
        self.label_comision_colocadora.grid(row=2, column=1)

        self.spin_tomadora = tk.Spinbox(self.ventana, from_=1, to=5.0,
                                        textvariable=self.spin_tomadora,
                                        increment=0.5,
                                        state='readonly')
        self.spin_tomadora.grid(row=1,column=2)

        self.spin_colocadora = tk.Spinbox(self.ventana, from_=0, to=2,
                                          textvariable=self.spin_colocadora,
                                          increment=0.2,
                                          state='readonly')
        self.spin_colocadora.grid(row=2, column=2)


class Table_Widget:

    def __init__(self, ventana):
        self.ventana = ventana
        self.table_wiget = None

        self.df = self.crear_df()

        self.dibujar_spin()

    def crear_df(self):
        columnas = [
            "Venta",
            "Compra",
            "Spread TNA %",
            "Spread %",
            "Spread Last %",
            "P&L $",
            "Caucion $",
            "Comision $",
            "Venta $",
            "Compra $"
        ]

        data = [
            ["AL30-CI", "AL30-48hs", 203.48, 0.07, -0.23, 1007, 467.347, 1676, 15525.20, 15510.80],
            ["GD30-CI", "GD30-48hs", 139.06, -0.40, 0.38, 346, 302210, 663, 23440.5, 23535.00]
        ]

        df = pd.DataFrame(data, columns=columnas)
        return df


    def dibujar_spin(self):
        self.table_wiget = tk.Text(self.ventana)
        self.table_wiget.insert(tk.INSERT, self.df.to_string())

        # Si quito el pack la ventana queda vacia.
        # Aun dejandolo se ve mal, la caja de texto queda angosta.
        self.table_wiget.pack()

        print(self.df)



def init():
    if __name__ == '__main__':
        root = tk.Tk()
        root.title('Ventana Principal')
        root.iconbitmap(default='favicon.ico')
        #b = Ejemplo_RadioButton(root)
        b = Ejemplo_SpinBox(root)

        #b = Table_Widget(root)

        # Main loop q controla ventana y eventos
        root.mainloop()

init()
