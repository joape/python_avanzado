import matematicas


def main():
    area_circulo = matematicas.calcular_area_circulo(5)
    area_rectangulo = matematicas.calcular_area_rectangulo(4, 6)

    print(f"Área del círculo: {area_circulo}")
    print(f"Área del rectángulo: {area_rectangulo}")
    matematicas.sumar(5, 3)
    # print(matematicas.pi)


main()
