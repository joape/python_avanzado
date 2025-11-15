"""
Solución ejercicio de clase 2, 22_ejercicio.py
"""

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def validar_numero(mensaje: str) -> int:
    logging.debug("Validando número")
    while True:
        numero_str = input(mensaje)
        if numero_str.strip().isdecimal():
            return int(numero_str)
        else:
            logging.info("❌ No se ingresó un número entero")
            continue


def ingresar_numeros() -> tuple[int, int]:
    """Solicita al usuario dos número y los devuelve como tupla"""
    logging.debug("Ingresando números")
    n1 = validar_numero("Ingresa el primer número: ")
    n2 = validar_numero("Ingresa el segundo número: ")
    return n1, n2


def verificar_multiplo(n1: int, n2: int) -> bool | None:
    logging.debug("Verifando múltiplo")
    if n2 == 0:
        logging.error("❌ El segundo número no puede ser cero")
        return None
    return n1 % n2 == 0


def mostrar_resultado(n1: int, n2: int, es_multiplo: bool) -> None:
    logging.debug("Mostrando resultado")
    if es_multiplo:
        print(f"{n1} SÍ es múltiplo de {n2}")
    else:
        print(f"{n1} NO es múltiplo de {n2}")

    # print(f"{n1} SÍ es múltiplo de {n2}" if es_multiplo else f"{n1} NO es múltiplo de {n2}")


def main():
    logging.debug("Inicio de programa")
    n1, n2 = ingresar_numeros()
    es_multiplo = verificar_multiplo(n1, n2)
    if es_multiplo is None:
        print("❌ No se pudo verificar si es múltiplo")
    else:
        mostrar_resultado(n1, n2, es_multiplo)


main()
