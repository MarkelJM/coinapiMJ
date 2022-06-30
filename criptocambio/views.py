from tkinter import *
from tkinter import ttk




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
        ejemplo = ttk.Label(self, text= "Criptocambio")
        ejemplo.grid(row=0, column=0)
