print(__name__)
import matematicas


def main():
    area_circulo = matematicas.calcular_area_circulo(5)
    area_rectangulo = matematicas.calcular_area_rectangulo(4, 6)
    area_ovalo = matematicas.calcular_area_ovalo(3, 2)

    print(f"Área del círculo: {area_circulo}")
    print(f"Área del rectángulo: {area_rectangulo}")
    print(f"Área del óvalo: {area_ovalo}")
    matematicas.sumar(5, 3)
    # print(matematicas.pi)


if __name__ == "__main__":
    main()
