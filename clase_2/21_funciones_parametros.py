def crear_mensaje_saludo(nombre: str, edad: int) -> str:
    mensaje = f"Hola {nombre}!, así que tienes {edad} años de edad?"
    return mensaje


def ingresar_datos_persona() -> tuple[str, int]:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    return nombre, edad


def saludar(mensaje_saludo: str) -> None:
    print(mensaje_saludo)


def main():
    nombre, edad = ingresar_datos_persona()
    mensaje_saludo = crear_mensaje_saludo(nombre, edad)
    saludar(mensaje_saludo)


main()
