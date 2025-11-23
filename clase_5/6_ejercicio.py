"""
✨ EJERCICIO ✨
Crear las siguientes clases con dataclass
    - Especie
        nombre: str
    - Animal
        especie: Especie
        nombre: str
        sonido: str
"""

from dataclasses import dataclass


@dataclass
class Especie:
    nombre: str


@dataclass
class Animal:
    especie: Especie
    nombre: str
    sonido: str


especie = Especie("Felino")

gato = Animal(especie, "Gardfield", "miau")
print("Especie", gato.especie.nombre)
print("Nombre", gato.nombre)
print("Sonidio", gato.sonido)
