"""
- Usar funciones con anotaciones de tipo (type hints)
- Crear una lista de productos
- Solicitar al usuario si desea comprar un producto
(hacerlo uno por uno)
- Todo lo que el usuario compre, guardarlo en un carrito (lista)
- Al finalizar, el usuario se excede con la compra y debe elegir
un producto para quitar del carrito, elegirlo y mostrarlo
"""

def mostrar_productos(productos: list[str]) -> None:
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto}")


def seleccionar_producto(productos: list[str]) -> str:
    while True:
        opcion = input("Ingrese el número del producto que desea comprar (0 para terminar): ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 0:
                return ""
            if 1 <= opcion <= len(productos):
                return productos[opcion - 1]
        
        print("❌ Entrada inválida. Ingrese solo un número válido.\n")


def quitar_producto(carrito: list[str]) -> None:
    print("\nCarrito actual:")
    for i, producto in enumerate(carrito, 1):
        print(f"{i}. {producto}")
    
    while True:
        opcion = input("Ingrese el número del producto que desea quitar: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(carrito):
                eliminado = carrito.pop(opcion - 1)
                print(f"Has quitado: {eliminado}")
                break
        
        print("❌ Entrada inválida. Ingrese solo un número válido.\n")


def main() -> None:
    productos = ["Pan", "Leche", "Huevos", "Queso", "Manzanas", "Café"]
    carrito: list[str] = []

    print("Bienvenido a la tienda")

    while True:
        mostrar_productos(productos)
        producto = seleccionar_producto(productos)
        if producto == "":
            break
        carrito.append(producto)
        print(f"✅ Agregaste {producto} al carrito.\n")

    if not carrito:
        print("El carrito está vacío.")
        return

    print("\nTu carrito final es:")
    for p in carrito:
        print(f"- {p}")

    print("\n Te excediste con la compra...")
    quitar_producto(carrito)

    print("\nCarrito final después de quitar un producto:")
    for p in carrito:
        print(f"- {p}")

    print("\n¡Gracias por tu compra!")

main()
