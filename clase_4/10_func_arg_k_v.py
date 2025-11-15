# v1


def saludar(nombre: str, apellido: str) -> None:
    print(nombre, apellido)


saludar(nombre="juan", apellido="perez")


# v2


def saludar_v2(nombre: str, apellido: str, edad=None) -> None:
    print(nombre, apellido, edad)


saludar_v2(nombre="juan", apellido="perez", edad=39)

# v3


def saludar_v3(**kwargs) -> None:
    print(kwargs)


saludar_v3(nombre="Juan", edad=39, altura=1.80, activo=True)
