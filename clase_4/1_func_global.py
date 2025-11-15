numero = 10


def cuadrado():
    global numero
    numero = numero + 1
    return numero**2


resultado = cuadrado()
print("El resultado de la suma es:", resultado)
