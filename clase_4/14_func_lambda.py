def normalizar():
    nombres = ["  juan", "  MAríA ", " peDro", "LUCÍA    "]
    print("Normalizados:", list(map(lambda nombre: nombre.strip().title(), nombres)))


def filtrar():
    nombres = ["  juan", "  MAríA ", " peDro", "LUCÍA    "]
    print(
        "Filtro:", list(filter(lambda nombre: nombre.strip().startswith("M"), nombres))
    )


normalizar()
filtrar()
