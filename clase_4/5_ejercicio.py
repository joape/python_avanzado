"""
Crear una función que reciba un diccionario y transformar sus
valores en mayúsculas.
Se debe crear un diccionario con 2 elementos cuyos valores sean cadenas.
Pasarlo como argumento a la función.
Debo guardar en una variable la devolución de la función.
Imprimir el diccionario original y luego el transformado.
"""

def transformar_mayusculas(datos:dict) -> dict:
    """Transforma los valores de un diccionario a mayúsculas."""
    if not isinstance(datos, dict):
        raise Exception ("El argumento debe ser un diccionario.")
    
    diccionario = datos
    nuevo_diccionario = diccionario.copy()
    for clave, valor in nuevo_diccionario.items():
        nuevo_diccionario[clave] = valor.upper()
    
    return nuevo_diccionario


# Creo diccionario con 2 elementos
mi_diccionario = {"nombre": "joaquin", "ciudad": "montevideo"}

# Guardo la devolución de la función en una variable
diccionario_transformado = transformar_mayusculas(mi_diccionario)

# Imprimo diccionario original y transformado
print("Diccionario original:", mi_diccionario)
print("Diccionario transformado:", diccionario_transformado)