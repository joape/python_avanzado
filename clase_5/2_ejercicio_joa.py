"""
- Crear una clase Persona
  que contenga los atributos / variables de instancia:
    - nombre: str
    - edad: int
- Crear 3 instancias de Persona
- Mostrar por terminal un mensaje de bienvenida para cada persona
"""
class Persona:
    def __init__(self, nombre: str, edad: int):  # constructor
        self.nombre = nombre
        self.edad = edad  


persona1 = Persona(nombre="Joaquin", edad=47)
persona2 = Persona(nombre="Esteban", edad=45)
persona3 = Persona(nombre="Maria", edad=28)
print(f"Bienvenido, {persona1.nombre}! Tienes {persona1.edad} años.")
print(f"Bienvenido, {persona2.nombre}! Tienes {persona2.edad} años.")
print(f"Bienvenido, {persona3.nombre}! Tienes {persona3.edad} años.")
