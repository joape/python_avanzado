def mostrar_entero(valor):
    print(f"Valor recibido: {valor}")
    valor += 10
    print(f"Valor modificado dentro de la función: {valor}")


entero = 5
print(f"Valor antes de llamar a la función: {entero}")
mostrar_entero(entero)
print(f"Valor después de llamar a la función: {entero}")
