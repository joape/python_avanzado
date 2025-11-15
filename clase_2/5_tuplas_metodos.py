# Métodos de las tuplas

serie_fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)
print(f"{serie_fibonacci=}")

print(serie_fibonacci.__len__())
print(len(serie_fibonacci))

# count()
# Devuelve el número de veces que existe un elemento en una tupla
cuenta = serie_fibonacci.count(1)
print(f"{cuenta=}")

# index()
valor_a_buscar = 8
indice = serie_fibonacci.index(valor_a_buscar)
print(f"El valor {valor_a_buscar} está en el índice {indice}")