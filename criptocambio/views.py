from tkinter import *
from tkinter import StringVar, ttk

from . import MONEDA




class CriptoView:
    

    def pedir_monedas(self):
        origen = input("moneda origen: ")
        destino = input("que moneda obtener: ")
        return(origen, destino)


    def mostrar_cambio(self, origen, destino, cambio):
        print("un {} vale como {:,.2f} {}".format(
            origen,cambio, destino
            ))

    def quieres_seguir(self):
        seguir = input("Quieres cambiar algo mas?  (S/N)  ")
        return seguir.upper()




class CriptoviewTk(ttk.Frame):
    def __init__(self,padre):
        super().__init__(padre, width=400, height=400)
        self.grid()
        self.crear_controles()

    def crear_controles(self):
               

        # entrada moneda origen
        self.origen = StringVar()
        etiqueta_entrada = ttk.Label(self, text = "Moneda origen").grid(row=0, column=0)        
        cambio_entrada = ttk.Combobox(self, values=MONEDA,textvariable=self.origen).grid(row=1, column=0)

        # entrada moneda destino
        self.destino = StringVar()
        etiqueta_destino = ttk.Label(self, text = "Moneda destino").grid(row=0, column=1)  
        cambio_destino = ttk.Combobox(self, values=MONEDA, textvariable=self.destino).grid(row=1, column=1)

        #etiqueta para el resultado        
        self.etiqueta_resultado = ttk.Label(self, text = "0.0", padding=10)
        self.etiqueta_resultado.grid(row=2, column=0, columnspan=2)

        #boton para el cambio
        self.boton_calcular = ttk.Button(self, text="Calcular", command=self.lo_que_hace_el_boton)
        self.boton_calcular.grid(row = 3, column= 1)

    def moneda_origen(self):
            return self.origen.get()[:3]

    def moneda_destino(self):
            return self.destino.get()[:3]

    def lo_que_hace_el_boton(self):
        print("La moneda origen", self.moneda_origen())
        print("La moneda destino", self.moneda_destino())



