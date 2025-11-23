"""
A partir del siguiente código, crear un método __str__ y la función main().
Crear una lista de usuarios e iterar y usar print() para invocar el método __str__
class Usuario:  # estilo UpperCamelCase
    def __init__(self, nombre_usuario, contraseña):  # método constructor
        self.nombre_usuario = nombre_usuario  # variable de instancia / atributo
        self.contraseña = contraseña  # # variable de instancia / atributo

user1 = Usuario("admin", 123)  # se crea un objeto / instanciación
user2 = Usuario("user", 789)
"""

class Usuario:  # estilo UpperCamelCase
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña 

    def __str__(self):  # método para representar el objeto como cadena
        return f"Usuario: {self.nombre_usuario}, Contraseña: {self.contraseña}"

def main():
    usuarios = [Usuario("admin", 123), Usuario("user", 789)]  #creo la lista de usuarios
    for usuario in usuarios:  # itero sobre la lista
        print(usuario)  # invocar el método __str__

if __name__ == "__main__":
    main()  # Poner para que no me pase como en el ejercicio anterior
