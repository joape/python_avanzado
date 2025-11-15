# Entrada
nombre = "Flor"
edad = 19

# Operaciones
validar_nombre = nombre != "****"
validar_nombre_longitud = len(nombre) >= 4 and len(nombre) < 8
validar_edad = edad > 5 and edad < 20
validar_edad_calculada = (edad * 3) > 35

validar = validar_nombre and validar_nombre_longitud and validar_edad and validar_edad_calculada

# Salida
print(validar)
