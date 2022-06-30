
from tkinter import *
from .models import CriptoModel
from .views import CriptoView, CriptoviewTk


class CriptoController:
    def __init__(self):
        self.modelo = CriptoModel()
        self.vista = CriptoView()

    def consultar(self):
        seguir = "S"
        while seguir == "S":
            desde, hasta = self.vista.pedir_monedas()
            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            self.modelo.consultar_cambio()
            self.vista.mostrar_cambio(desde, hasta, self.modelo.cambio)

            seguir = ""
            while seguir not in ("S", "N"):
                 seguir = self.vista.quieres_seguir()


class CriptoControllerTk(Tk):
    def __init__(self):
        super().__init__()
        self.vista = CriptoviewTk(self, self.calcular_cambio)
        self.modelo =CriptoModel()


    def run(self):
        self.mainloop()

    def calcular_cambio(self):
        
        self.modelo.moneda_origen = self.vista.moneda_origen()
        self.modelo.moneda_destino = self.vista.moneda_destino()
        self.modelo.consultar_cambio()
        self.vista.mostrar_cambio(self.modelo.cambio)
        
