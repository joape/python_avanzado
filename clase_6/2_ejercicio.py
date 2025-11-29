class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.contraseña = contraseña

    def __str__(self) -> str:
        return self.nombre

    def set_nombre(self, nuevo_valor: str):  # método de instancia
        self.nombre = nuevo_valor

    def set_contraseña(self, nuevo_valor: str):
        self.contraseña = nuevo_valor


def main():
    usuario_1 = Usuario("admin", "123")
    usuario_2 = Usuario("juan", "789")
    usuario_3 = Usuario("pepe", "555")
    usuarios = (usuario_1, usuario_2, usuario_3)
    for usuario in usuarios:
        print(f"{usuario} ({usuario.contraseña})", end=" ")

    print()
    usuario_1.set_nombre("superadmin")
    usuario_1.set_contraseña("*123*")
    for usuario in usuarios:
        print(f"{usuario} ({usuario.contraseña})", end=" ")


main()

# Crear un método de instancia para establecer una nueva contraseña
