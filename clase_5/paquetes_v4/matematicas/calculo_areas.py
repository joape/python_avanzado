__all__ = ["calcular_area_circulo", "calcular_area_rectangulo", "calcular_area_ovalo"]

from math import pi

from .mis_constantes import PHI  # importación relativa

# from matematicas.mis_constantes import PHI  # importación absoluta


def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    return pi * radio**2


def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura


def calcular_area_ovalo(semi_eje_mayor: float, semi_eje_menor: float) -> float:
    """Calcula el área de un óvalo dado sus semi-ejes mayor y menor."""
    return PHI * semi_eje_mayor * semi_eje_menor


if __name__ == "__main__":
    print("Ejecutando calculo_areas.py")
    print(f"Valor de PHI: {PHI}")
    print(f"Área del círculo de radio 3: {calcular_area_circulo(3)}")
    print(f"Área del rectángulo de base 4 y altura 5: {calcular_area_rectangulo(4, 5)}")
    print(f"Área del óvalo de semi-ejes 2 y 3: {calcular_area_ovalo(2, 3)}")
