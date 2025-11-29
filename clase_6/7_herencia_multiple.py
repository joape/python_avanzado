class Vehiculo:
    def andar(self):
        print("El vehículo está en movimiento.")


class Auto(Vehiculo):
    def tocar_bocina(self):
        print("El auto está tocando la bocina.")


class VirarABaborMixin:
    def virar_a_babor(self):
        print("Virando a babor")


class VirarAEstriborMixin:
    def virar_a_estribor(self):
        print("Virando a estribor")


class Lancha(Vehiculo, VirarABaborMixin, VirarAEstriborMixin):
    pass


auto = Auto()
auto.andar()
auto.tocar_bocina()

lancha = Lancha()
lancha.andar()
lancha.virar_a_babor()
lancha.virar_a_estribor()
