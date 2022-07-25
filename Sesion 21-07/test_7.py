

#200: ok
#404: error de permisos
#500: error con el servidor
import requests


res = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

print(res.status_code)
print(res.headers)
json = res.json()

print(json)
