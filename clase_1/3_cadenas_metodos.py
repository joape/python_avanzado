que_es_python = " pithon es un lenguaje de programación interpretado  "

print(que_es_python.upper())
print(que_es_python.strip().capitalize())
print(que_es_python.strip().capitalize().count("P"))

print(que_es_python.replace("e", "3"))
que_es_python = que_es_python.replace("pithon", "Python")
print(que_es_python)

print("0123456789".isdigit())
print(" 0123456789".isdigit())
print("abcde".isalpha())

lista = "Debo practicar Python todos los días".split()
print(lista)
nueva_cadena = " - ".join(lista)
print(nueva_cadena)


a = 2
b = 3
print(f"La suma de {a} + {b} = {a + b}")

from math import pi

print(f"{pi:.2f}")

print(f"{232323:>10}")
print(f"{1212:>10}")


print(f"{232323:<2}")
print(f"{1212:<2}")

print(f"{23232334343:^40}")
print(f"{1212:^40}")
