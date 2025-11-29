class Guitarra:
    def tocar(self):
        print("tin tin tin")


class GuitarraElectrica(Guitarra):
    def tocar_con_distorsion(self):
        print("tron tron tron")


class GuitarraElectricaConBajo(GuitarraElectrica):
    def tocar_bajo(self):
        print("bun bun bun")


guitarra = Guitarra()
guitarra.tocar()
print()
guitarra_elec = GuitarraElectrica()
guitarra_elec.tocar()
guitarra_elec.tocar_con_distorsion()
print()
guitarra_elec_bajo = GuitarraElectricaConBajo()
guitarra_elec_bajo.tocar()
guitarra_elec_bajo.tocar_bajo()
guitarra_elec_bajo.tocar_con_distorsion()
