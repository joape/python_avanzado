from dataclasses import dataclass


@dataclass
class Ciudad:
    nombre: str
    habitantes: int


@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad: Ciudad


mendoza = Ciudad(nombre="Mendoza", habitantes=2_000_000)
persona = Persona(nombre="Juan", edad=20, ciudad=mendoza)

print(persona)
