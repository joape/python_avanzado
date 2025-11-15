""" Crear un bucle que almacene en una variable la
suma de todos los elementos numéricos de una
lista, con excepción del último."""

numeros = [12,10,5,4,8,9,7,6,3,2,15,54,66,44,33,1]
suma = 0

for numero in numeros[:-1]:
    suma+= numero

print(suma)