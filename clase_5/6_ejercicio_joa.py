from dataclasses import dataclass

@dataclass
class Especie:
    nombre: str

@dataclass
class Animal:
    especie: Especie
    nombre: str
    sonido: str

if __name__ == "__main__":
    especie_perro = Especie("Cimarron Uruguayo")
    perro = Animal(especie_perro, "Malebo", "guau")
    print(perro)
