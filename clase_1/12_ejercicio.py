"""
Una empresa debe aprobar o no un crédito para un cliente.
Las condiciones son las siguientes:
    - El cliente debe ser mayor de edad.
    - Debe tener una antigüedad en el sistema financiero mínimo de 3 años
    y un ingreso mayor a 2500 dólares.
    - En caso de que no tenga la antigüedad suficiente,
    su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito.
"""

edad = int(input("Edad: "))
antiguedad_laboral = int(input("Antigüedad laboral (años): "))
ingreso_mensual = float(input("Ingreso mensual: "))

es_adulto = edad >= 18
caso_1 = es_adulto and antiguedad_laboral >= 3 and ingreso_mensual > 2500
caso_2 = es_adulto and ingreso_mensual >= 4000

if caso_1 or caso_2:
    print("Crédito aprobado")
else:
    print("Crédito no aprobado")
