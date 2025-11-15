import json

with open("22_json.json") as archivo:
    datos: list = json.load(archivo)

mi_dict = {"name": "Dani", "age": 50, "city": "Madrid", "active": True}
mi_dict_2 = {"name": "Darío", "age": 17, "city": "Barcelona", "active": True}
datos.append(mi_dict)
datos.append(mi_dict_2)

with open("22_json.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
