class CriptoView:
    

    def pedir_monedas(self):
        origen = input("moneda origen: ")
        destino = input("que moneda obtener: ")
        return(origen, destino)


    def mostrar_cambio(self, origen, destino, cambio):
        print("un {} vale como {:,.2f} {}".format(
            origen,cambio, destino
            ))
