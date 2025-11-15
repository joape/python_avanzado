# TUPLE

numeros_primos = (1, 3, 5)

print(numeros_primos)
print(numeros_primos[0]) # slicing
print(numeros_primos[1])
print(numeros_primos[2])

# primero = numeros_primos[0]
# segundo = numeros_primos[1]
# tercero = numeros_primos[2]
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)

print("Desempacar más elementos:")
numeros_primos = (1, 3, 5, 7, 11, 13)
primero, segundo, *resto = numeros_primos
print(primero, segundo, resto)

print("Desempacar más elementos v2")
numeros_primos = (1, 3, 5, 7, 11, 13)
primero, *medio, ultimo = numeros_primos
print(primero, medio, ultimo)