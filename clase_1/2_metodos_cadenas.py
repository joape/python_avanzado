que_es_python = " Python es un lenguaje de programacion interpretado "
#print(type(que_es_python))

print(que_es_python.upper())
print(que_es_python.strip().capitalize())
print(que_es_python.strip().capitalize().count("P"))
print(que_es_python.replace("e", "3"))
que_es_python = que_es_python.replace("pithon", "Python")
print(que_es_python)

print("0123456789".isdigit())
print(" 0123456789".isdigit())
print("abcde".isalpha())

print("Debo practicar Python todos los dias".split("Python"))

lista = "Debo practicar Python todos los dias".split()
print(lista)
nueva_cadena = " - ".join(lista)
print(nueva_cadena)

a = 2
b = 3
print(f"La suma de {a} + {b} = {a + b}")

