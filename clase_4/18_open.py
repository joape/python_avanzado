archivo = open("18_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django")
archivo.close()

archivo = open("18_test.txt", "r")
lectura = archivo.read()
archivo.close()

print(lectura)
