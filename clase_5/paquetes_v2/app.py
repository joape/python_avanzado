import clientes


def main():
    nombre_a_buscar = input("Ingrese el nombre del cliente a buscar: ")
    cliente = clientes.buscar(nombre_a_buscar)
    if cliente:
        print("Cliente encontrado:")
        for clave, valor in cliente.items():
            print(f"{clave}: {valor}")
    else:
        print("Cliente no encontrado.")


main()
