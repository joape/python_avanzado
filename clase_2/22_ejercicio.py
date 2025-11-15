"""
A partir del siguiente código, identificar cada parte y crear funciones.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 % n2 == 0:
    print(f"{n1} es múltiplo de {n2}")
else:
    print(f"{n1} no es múltiplo de {n2}")
"""
def ingresar_datos() -> tuple[int, int]:
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    return n1, n2

def calcular_modulo(n1: int, n2: int) -> str:    
    if n1 % n2 == 0:
        mensaje= f"{n1} es múltiplo de {n2}"
    else:
        mensaje= f"{n1} no es múltiplo de {n2}"
    
    return mensaje

def mostrar_mensaje(mensaje: str) -> None:
    print(mensaje)

def main():
    n1, n2 = ingresar_datos()
    mensaje = calcular_modulo(n1, n2)
    mostrar_mensaje(mensaje)

main()