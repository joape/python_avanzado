diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}

# get: obtiene el valor de una clave, si no existe devuelve un valor por defecto
# (None o el que se pase)
# print(diccionario["nombres"]) # KeyError
# print(diccionario.get("nombres")) # None
print(diccionario.get("nombre"))

# update(dict)
# actualiza el diccionario con los pares clave-valor del dict pasado
diccionario.update({"edad": 31, "email": "juan.example.com"})
diccionario.update(ciudad="Barcelona")
print(diccionario)

# pop(clave, valor_por_defecto)
# elimina la clave y devuelve su valor. Si no existe devuelve el valor por defecto
valor = diccionario.pop("activo")
print("Valor eliminado:", valor)
print(diccionario)
