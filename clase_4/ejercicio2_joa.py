"""
A partir del siguiente código, crear un bloque
try-except para que muestre "el archivo no existe"
archivo = open("2_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()
archivo = open("2_test.tx", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
"""