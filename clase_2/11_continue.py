caja_de_herramientas = [
    "martillo",
    "destornillador",
    "sierra",
    "tornillos",
    "tuercas",
    "taladro",
]

for herramienta in caja_de_herramientas:
    if herramienta.startswith("des"):
        continue
    if herramienta.startswith("tu"):
        break
    print(herramienta)