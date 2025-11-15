# Métodos de las listas

serie_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print(f"{serie_fibonacci=}")

# append(): agrega un elemento al final de la lista
numero_siguiente = serie_fibonacci[-1] + serie_fibonacci[-2]
serie_fibonacci.append(numero_siguiente)
print(f"append: {serie_fibonacci=}")

# extend(): extiende la lista agregando los elementos de otra lista
mas_numeros = (233, 377, 610)  # puede ser una tupla o cualquier iterable
serie_fibonacci.extend(mas_numeros)
print(f"extend: {serie_fibonacci=}")

# insert(): inserta un elemento en una posición específica
indice_que_busco = 0
serie_fibonacci.insert(indice_que_busco, "inicio") # type:ignore
print(f"insert: {serie_fibonacci=}")

# remove(): elimina la primera aparición de un valor específico
serie_fibonacci.remove("inicio") # type:ignore
print(f"remove: {serie_fibonacci=}")

# pop(): elimina y devuelve el elemento en una posición específica (por defecto, el último)
elemento_eliminado = serie_fibonacci.pop()
print(f"pop: {serie_fibonacci=}\nelemento eliminado: {elemento_eliminado}")

# sort(): ordena los elementos de la lista (solo si son comparables entre sí)
numeros = [5, 2, 9, 1, 5, 6]
print(f"antes de sort: {numeros=}")
numeros.sort()
print(f"después de sort: {numeros=}")

# reverse(): invierte el orden de los elementos en la lista
numeros.reverse()
print(f"después de reverse: {numeros=}")

# count(): cuenta cuántas veces aparece un valor específico en la lista
veces_cinco = numeros.count(5)
print(f"count: el número 5 aparece {veces_cinco} veces en {numeros=}")

# index(): devuelve el índice de la primera aparición de un valor específico
indice_que_busco = 9
indice_encontrado = numeros.index(indice_que_busco)
print(f"index: el número 9 está en el índice {indice_encontrado} de {numeros=}")

# clear(): elimina todos los elementos de la lista
# serie_fibonacci = []
# print(serie_fibonacci)
serie_fibonacci.clear()
print(f"clear: {serie_fibonacci=}")
