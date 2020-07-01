import requests
import json

for i in range(1,17):   
 url = "https://swapi.dev/api/people/"+ str(i)
 payload = {}
 headers= {}
 response = requests.request("GET", url, headers=headers, data = payload)
 x =json.loads(response.text)
 print("{name} {gender} {homeworld}".format(
        name=x["name"],
        gender=x["gender"],
        homeworld=x["homeworld"]
    ))

