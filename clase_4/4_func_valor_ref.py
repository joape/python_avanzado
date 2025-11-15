def modificar_lista(coleccion: list):
    print(f"Lista recibida: {coleccion}")
    coleccion.append(4)
    print(f"Lista modificada dentro de la función: {coleccion}")


mi_lista = [1, 2, 3]
print(f"Lista antes de llamar a la función: {mi_lista}")
modificar_lista(mi_lista.copy())
print(f"Lista después de llamar a la función: {mi_lista}")

# list().copy()
# set().copy()
# dict().copy()
# tuple() no tiene método copy ya que es inmutable
# str() no tiene método copy ya que es inmutable
# int() no tiene método copy ya que es inmutable
# float() no tiene método copy ya que es inmutable
