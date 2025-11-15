"""
A partir de la siguiente lista:
matriz:
matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]
Sumar los elementos de cada sublista, y agregar el resultado
al final de cada una de las sublistas.
La estructura final es la siguiente:
matriz = [
    [1, 20, 3, 24],
    [4, 3, 2, 9],
    [10, 4, 1, 15],
]
Puedes usar la función sum(<lista>)
"""
matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

for lista in matriz:
    lista.append(sum(lista))

print(matriz)
