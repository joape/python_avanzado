print(__name__)


def sumar(a, b):
    print(a + b)


def restar(a, b):
    print(a - b)


def multiplicar(a, b):
    print(a * b)


def dividir(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Error: División por cero")


if __name__ == "__main__":
    dividir(10, 2)
    dividir(10, 0)
