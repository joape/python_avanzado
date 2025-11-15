"""
Crear una función que reciba argumentos indeterminados que
sean alturas de personas, crear una lista y ordenarla de menor a mayor
y devolver la lista ordenada
Usar isinstance para validar que los argumentos sean de tipo numerico
"""

from typing import Any


def ordenar_alturas(*args: Any) -> list[float]:
    """Recibe alturas, toma las que sean numéricas y devuelve alturas ordenadas"""
    alturas_validas: list[float] = []
    for i in args:
        if isinstance(i, int | float) and not isinstance(i, bool):
            alturas_validas.append(i)
    alturas_validas.sort()
    return alturas_validas


def main():
    alturas_ordenadas_float = ordenar_alturas(1.75, "1.80", 1.65, 1.90, True, 1.70)
    alturas_ordenadas_str = map(lambda altura: f"{altura}m", alturas_ordenadas_float)
    print(f"Alturas ordenadas: {', '.join(alturas_ordenadas_str)}")


main()
