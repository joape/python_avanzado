"""
Consigna:
Crear una variable llamada comando
La variable contendrá el texto: 'upper()'
Mostrar 3 veces por la terminal el mensaje:
"La función upper() sirve para poner en mayúsculas las cadenas."
Usar 3 print(), usando las 3 formas concatenación, +, coma, f-string
"""

comando = 'upper()'

print("La funcion " + comando + " sirve para poner en mayúsculas las cadenas.")
print("La funcion" , comando , "sirve para poner en mayúsculas las cadenas.")
print(f"La funcion {comando} sirve para poner en mayúsculas las cadenas.")
print("La funcion {} sirve para poner en mayúsculas las cadenas.".format(comando))
