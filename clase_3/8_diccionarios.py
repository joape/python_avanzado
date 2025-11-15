# Diccionarios
# Un diccionario es una estructura de datos que almacena pares clave-valor. Es mutable.

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}

print(diccionario)
print(len(diccionario))

# Acceso a valores
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["lenguajes"])

# Crear
diccionario["email"] = "juan@example.com"

# Modificar
diccionario["edad"] += 1

# Eliminar
del diccionario["activo"]
print(diccionario)

# Desempaquetado de diccionarios

datos_civiles = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Barcelona",
}
datos_estudios = {
    "carrera": "Ingeniería Informática",
    "universidad": "Universidad de Barcelona",
    "idiomas": ["Español", "Inglés"],
}

datos_completos = {**datos_civiles, **datos_estudios}
from pprint import pprint

pprint(datos_completos)

español = datos_completos["idiomas"][0]
ingles = datos_completos["idiomas"][1]
print(español)
print(ingles)
