diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}

# keys
for k in diccionario.keys():
    print("Clave:", k)

# values
for v in diccionario.values():
    print("Valor:", v)

# items
for k, v in diccionario.items():
    if isinstance(v, list):
        v = ", ".join(v)
    if isinstance(v, bool):
        v = "Sí" if v else "No"
    print(f"{k:>20} - {v}")
