# archivo = open("18_test.txt", "w")
# archivo.write("Python\n")
# archivo.write("Django")
# archivo.close()

with open("20_test.txt", "w") as archivo:
    archivo.write("Python\n")
    archivo.write("Django")
    # no hace falta cerrar con close()
