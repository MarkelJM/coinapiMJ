import requests

apikey = "8A4D11CB-8D41-43A0-8C69-708A76BD6A2A"
headers = {'X-CoinAPI-Key' : apikey

}

api_url = "http://rest.coinapi.io"
endpoint = "/v1/assets"

url = api_url +endpoint

#respuesta será lo que devuelve el servidor con nuestra llamda del url
respuesta = requests.get(url, headers=headers)
codigo = respuesta.status_code

if codigo == 200:
    print("las monedas disponibles son:")
    respuesta_json = respuesta.json()

    for moneda in respuesta_json:
        if moneda["asset_id"].startswith("EUR"):
            print(moneda["asset_id"], moneda["name"])

else:
    print("La peticion a la API ha fallado")
    print(f"codigo del error {codigo}")
    print(f"razon del error: {respuesta.reason}")
    print(respuesta.text)
