class Calculos:
    def __init__(self) -> None:
        self.resultado: float | None = None

    @staticmethod
    def superficie_circulo(radio: float) -> float:
        return 3.14 * radio**2


mis_calculos = Calculos()

mis_calculos.resultado = Calculos.superficie_circulo(5.4)
print(mis_calculos.resultado)
