usuarios: list[dict] = [
    {
        "nombre": "Juan",
        "nacionalidades": ["argentina", "española"],
    },
    {
        "nombre": "María",
        "nacionalidades": ["colombiana"],
    },
    {
        "nombre": "Pedro",
        "nacionalidades": ["chilena"],
    },
    {
        "nombre": "Ana",
        "nacionalidades": ["uruguaya"],
    },
]

nacionalidad_española_de_juan = usuarios[0]["nacionalidades"][1]
print(nacionalidad_española_de_juan)
