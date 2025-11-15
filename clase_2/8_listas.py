# Listas: colección mutable de objetos indexados

from math import pi

lista = [1, float(f"{pi:.3f}"), "hola", True, [1, 2, 3], "python".title()]
print(lista)

# Create (crear elementos)
lista = lista + ["adiós"]
print(lista)

# Update (modificar elementos)
lista[-1] = "¡Adiós!"
print(lista)

# Delete (eliminar elementos)
del lista[0]
print("delete", lista)

# len()
print(len(lista))

# operador in
nueva_lista = [3.142, "hola", True, [1, 2, 3], "Python", "¡Adiós!"]
print(3.142 in nueva_lista)
print("computadora" not in nueva_lista)

# concatenación (mutabilidad)
lista1 = [1, 2, 3]
print(id(lista1))
lista2 = [4, 5, 6]
# lista1 = lista1 + lista2  # esto crea un nuevo objeto
lista1 += lista2
print(lista1)
print(id(lista1))