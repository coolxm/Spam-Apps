#imports
import requests

#request from api
astros = requests.get('http://api.open-notify.org/astros.json')


#More readable
astros_json = astros.json()
print(astros_json["number"])

for p in astros_json["people"]:
    print(p["name"])

