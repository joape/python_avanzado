"""
Crear un bucle while True que pida al usuario
un número. Si el número es menor a 1, salir del bucle
-> crear un bloque else que imprima "fin del programa"
"""

while True:
    numero = int(input("Ingresar un número: "))
    print(f"Tu número es: {numero}")
    if numero < 1:
        break
else:
    print("Final del programa")
