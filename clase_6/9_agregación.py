class Motor:
    def __init__(self, cilindrada: int):
        self.cilindrada = cilindrada

    def encender(self):
        print("El motor se ha encendido...")

    def apagar(self):
        print("El motor se ha apagado")


class Auto:
    def __init__(self, modelo: str, motor: Motor):  # agregación
        self.modelo: str = modelo
        self.motor: Motor = motor

    def arrancar(self):
        self.motor.encender()
        print("Auto arrancado...")

    def detener(self):
        self.motor.apagar()
        print("Auto detenido...")


mi_motor_mustang = Motor(cilindrada=5000)

mi_auto = Auto("Ford Mustang", mi_motor_mustang)
mi_auto.arrancar()
mi_auto.detener()
