matriz: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


# lista_aplanada: list[int] = []
# for sublista in matriz:
#     for numero in sublista:
#         lista_aplanada.append(numero)

lista_aplanada = [numero for sublista in matriz for numero in sublista]


print(matriz)
print(lista_aplanada)
