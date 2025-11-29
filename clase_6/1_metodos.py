class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.contraseña = contraseña
    def __str__(self) -> str:
        return self.nombre
    def set_nombre(self, nuevo_valor: str):  # método de instancia
        self.nombre = nuevo_valor

def main():
    usuario_1 = Usuario("admin", "123")
    usuario_2 = Usuario("juan", "789")
    usuario_3 = Usuario("pepe", "555")
    usuarios = (usuario_1, usuario_2, usuario_3)
    for usuario in usuarios:
        print(usuario, end=" ")
    print()
    usuario_1.set_nombre("superadmin")
    for usuario in usuarios:
        print(usuario, end=" ")

main()