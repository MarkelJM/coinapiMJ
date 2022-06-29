import requests


apikey = "8A4D11CB-8D41-43A0-8C69-708A76BD6A2A"
headers = {'X-CoinAPI-Key' : apikey
}



#respuesta será lo que devuelve el servidor con nuestra llamda del url
seguir = "S"
while seguir.upper()=="S":
    moneda_origen = input("moneda origen: ")
    moneda_destino = input("que moneda obtener: ")

    url = f"http://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}?time="
    respuesta = requests.get(url, headers=headers)

    tipo_cambio = respuesta.json()


    cambio = tipo_cambio["rate"]

    print("un {} vale como {:,.2f} {}".format(moneda_origen,cambio, moneda_destino))
    
    seguir = ""
    while seguir.upper not in ("S", "N"):
        seguir = input("quieres seguir con cambio? (S/N)")