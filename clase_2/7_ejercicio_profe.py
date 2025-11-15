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

from pprint import pprint

matriz: list[list[int]] = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

matriz[0] = matriz[0] + [matriz[0][0] + matriz[0][1] + matriz[0][2]]
matriz[1] = matriz[1] + [matriz[1][0] + matriz[1][1] + matriz[1][2]]
matriz[2] = matriz[2] + [matriz[2][0] + matriz[2][1] + matriz[2][2]]
pprint(matriz, width=40)


matriz: list[list[int]] = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]
matriz[0] = matriz[0] + [sum(matriz[0])]
matriz[1] = matriz[1] + [sum(matriz[1])]
matriz[2] = matriz[2] + [sum(matriz[2])]
pprint(matriz, width=40)