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
    def __init__(self, nombre_usuario, contraseña):  # método constructor
        self.nombre_usuario = nombre_usuario  # variable de instancia / atributo
        self.contraseña = contraseña  # # variable de instancia / atributo

    def __str__(self) -> str:
        return self.nombre_usuario


def main():
    user1 = Usuario("admin", 123)  # se crea un objeto / instanciación
    user2 = Usuario("user", 789)
    usuarios: list[Usuario] = [user1, user2]
    for usuario in usuarios:
        print(usuario)


main()
