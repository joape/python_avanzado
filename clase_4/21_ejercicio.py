"""
Crear un archivo que contenga los elementos de una lista.
La lista consiste en 5 elementos.
Usar for range para pedir los elementos de la lista
Usar for para iterar la lista y escribir sobre el archivo
"""

def main():
    lista = [''] * 5  # crear lista de 5 elementos
    for i in range(5):
        lista[i] = input(f"Elemento {i+1}/5: ").strip()

    with open("elementos.txt", "w", encoding="utf-8") as f:
        for item in lista:
            f.write(item + "\n")


main()