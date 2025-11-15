"""
A partir de dos variables llamadas nombre y edad:
crear una variable que almacene si se cumplen las siguientes condiciones,
y mostrar al usuario True o False:
    - nombre sea diferente de cuatro asteriscos ****
    - edad sea mayor que 5 y a su vez menor que 20
    - Que la longitud de nombre sea mayor o igual a 4 pero a la vez menor que 8
    - edad multiplicada por 3 sea mayor que 35
    - No debes usar funciones, condicionales, bucles o cualquier
    - otra instrucción que no hayamos visto
"""

nombre = "Joaquin"
edad = 47

#Operaciones
validar_nombre = nombre != "****"
validar_nombre_longitud = len(nombre) >=4 and len(nombre) < 8
validar_edad =  edad > 5 and edad < 20
validar_edad_calculada = (edad * 3) > 35

validar = validar_nombre and validar_nombre_longitud and validar_edad and validar_edad_calculada

#Salida
print(validar)


#Joaquin
#print(nombre != "****")
#print(edad > 5 and edad < 20)
#print(len(nombre) >= 4 and len(nombre) < 8)
#print(edad * 3 > 35) 
