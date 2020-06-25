import requests

url = "https://deckofcardsapi.com/api/deck/wso5fb9htogi/draw/?count=3"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data = payload)

print("El ID de tu mazo es:  " + (response.json()["deck_id"]))
print("Tus Cartas son:" + (str(response.json()["cards"])))
print(response.json())