"""
- Crear una clase Persona
  que contenga los atributos / variables de instancia:
    - nombre: str
    - edad: int

- Crear 3 instancias de Persona
- Mostrar por terminal un mensaje de bienvenida para cada persona
"""


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad


def crear_instancias() -> list[Persona]:
    pepe = Persona("Pepe", 50)
    juancito = Persona("Juan", 20)
    lucy = Persona("Lucía", 40)
    return [pepe, juancito, lucy]


def saludar_a_personas(personas: list[Persona]) -> None:
    for persona in personas:
        print(f"Hola {persona.nombre}!")


def main():
    personas = crear_instancias()
    saludar_a_personas(personas)


main()
