"""
A partir del siguiente código, crear un bloque
try-except para que muestre "el archivo no existe"

archivo = open("20_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()

archivo = open("20_test.tx", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
"""
archivo = open("20_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()

try:
    archivo = open("20_test.txt", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)
except FileNotFoundError:
    print("el archivo no existe")