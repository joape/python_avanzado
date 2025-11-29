class Motor:
    def __init__(self, cilindrada: int):
        self.cilindrada = cilindrada

    def encender(self):
        print("El motor se ha encendido...")

    def apagar(self):
        print("El motor se ha apagado")


class Auto:
    def __init__(self, modelo: str, cilindrada: int) -> None:
        self.modelo = modelo
        self.motor = Motor(cilindrada)  # composición

    def arrancar(self):
        self.motor.encender()
        print("Auto arrancando")

    def detener(self):
        self.motor.apagar()
        print("Auto detenido...")


mi_auto = Auto("Ford Mustang", cilindrada=5000)
mi_auto.arrancar()
mi_auto.detener()
