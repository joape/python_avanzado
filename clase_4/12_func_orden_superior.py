from typing import Callable


def transformar(lista: list, funcion: Callable[[str], str]) -> list[str]:
    # nueva_lista = []
    # for item in lista:
    #     nuevo_valor = funcion(item)
    #     nueva_lista.append(nuevo_valor)
    # return nueva_lista
    return [funcion(item) for item in lista]


def normalizar_str(nombre: str) -> str:
    return nombre.strip().title()


def agregar_prefijo(nombre: str) -> str:
    return f"Sr./Sra. {nombre}"


def main():
    nombres = ["  juan", "  MAríA ", " peDro", "LUCÍA    "]
    nombres_normalizados = transformar(nombres, normalizar_str)
    nombres_con_prefijos = transformar(nombres_normalizados, agregar_prefijo)
    print("Normalizados:", nombres_normalizados)
    print("Prefijos:", nombres_con_prefijos)


main()
