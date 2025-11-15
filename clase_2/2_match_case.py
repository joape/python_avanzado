dato = ["23"]

match dato:
    case int():
        print("Es un entero")
    case str():
        print("Es una cadena")
    case list():
        print("Es una lista")
    case _:
        print("No se reconoce la estructura de datos")