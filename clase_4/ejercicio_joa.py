"""
Crear una función que reciba argumentos indeterminados que
sean alturas de personas, crear una lista y ordenarla de menor a mayor
y devolver la lista ordenada
Usar isinstance para validar que los argumentos sean de tipo numerico
"""
def validar_numeros(*args: float) -> bool:
    """Valido que todos los argumentos sean numéricos"""
    return all(isinstance(altura, (int, float)) for altura in args)


def crear_lista_alturas(*alturas: float) -> list[float]:
    """Creo la lista a partir de los argumentos"""
    return list(alturas)


def ordenar_alturas(alturas: list[float]) -> list[float]:
    """Ordeno las alturas de menor a mayor"""
    return sorted(alturas)


def procesar_alturas(*alturas: float) -> list[float]:
    """Función principal que valida, crea y ordena las alturas"""
    if not validar_numeros(*alturas):
        raise TypeError("Todos los argumentos deben ser numéricos")
    
    lista = crear_lista_alturas(*alturas)
    return ordenar_alturas(lista)


def main():
    resultado = procesar_alturas(1.50, 2.0, 1.75, 1.60, 1.82, 1.70, 1.55)
    print(f"Alturas ordenadas: {resultado}")

main()