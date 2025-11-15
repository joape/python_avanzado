def mostrar_lista(coleccion: list):
    print(f"Lista recibida: {coleccion}")
    coleccion.append(4)
    print(f"Lista modificada dentro de la función: {coleccion}")


mi_lista = [1, 2, 3]
print(f"Lista antes de llamar a la función: {mi_lista}")
mostrar_lista(mi_lista)
print(f"Lista después de llamar a la función: {mi_lista}")
