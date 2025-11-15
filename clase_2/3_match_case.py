lista = [1, 2, 100]

match lista:
    case []:
        print("La lista está vacía")
    case [x, y]:
        print(f"La lista tiene 2 elementos: {x} y {y}")
        print(x + y)
    case [x, y, otro]:
        print(f"La lista tiene 3 elementos: {x} - {y} - {otro}")
        print(sum(lista))
    case _:
        print("No se reconoce la estructura")