import json

with open("22_json.json") as archivo:
    datos = json.load(archivo)

print(datos)
print(type(datos))
