from typing import Any


def funcion(parametro: Any, parametro2: Any, *args: int, **kwargs):
    print(parametro, parametro2)
    print(args)
    print(kwargs)


dato = {"username": "admin", "password": "123"}

funcion("hola", 123, 1, 2, 3, 4, language="spanish", **dato, **{"altura": 1.40})
