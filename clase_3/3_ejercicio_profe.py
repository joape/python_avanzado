"""
- Usar funciones con anotaciones de tipo (type hints)
- Crear una lista de productos
- Solicitar al usuario si desea comprar un producto
(hacerlo uno por uno)
- Todo lo que el usuario compre, guardarlo en un carrito (lista)
"""

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def comprar(productos: list[str]) -> list[str]:
    carrito_compras = []
    print("Escribir 's' para sí, o cualquier otra entrada para un no.")
    for producto in productos:
        entrada = input(f"¿Compra '{producto}'? ")
        if entrada.strip().lower().startswith("s"):
            carrito_compras.append(producto)
            logging.info(carrito_compras)
    return carrito_compras


def main():
    productos = ["Notebook", "Celular", "Tablet", "Auriculares"]
    carrito_compras = comprar(productos)
    print("Tu compra: " + ", ".join(carrito_compras))


main()
