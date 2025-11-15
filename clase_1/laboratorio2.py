"""Utilizando un bucle “while”, elaborar un código
que imprima en pantalla cada uno de los
elementos de una lista y simultáneamente los
elimine, hasta quedar vacía."""

lista = ['a',4,5,'b','joaquin','tadeo', 34,23,'Jimena']

while len(lista) > 0:
    print(lista[0])
    del(lista[0])

print(lista)