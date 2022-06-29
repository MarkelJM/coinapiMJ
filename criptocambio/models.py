import requests

from . import APIKEY

class APIError(Exception):
    pass

class CriptoModel:
    
    
    def __init__(self, origen, destino):
        self.moneda_origen = origen
        self.moneda_destino = destino
        self.cambio = 0.0




    def consultar_cambio(self):
        cabecera =  {'X-CoinAPI-Key' : APIKEY
        }
        
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}?time="
        respuesta = requests.get(url, headers=cabecera)

        if respuesta.status_code == 200:
            #guardar el cambio
            self.cambio = respuesta.json()["rate"]
        else:
            raise APIError(
                "Ha ocurrido un error {} {}  al consultar la API".format(respuesta.status_code, respuesta.reason)
                )
