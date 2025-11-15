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

edad_str = input("Ingrese su edad:")
antiguedad_str = input("Ingrese su antiguedad")
ingreso_str = input("Ingrese su sueldo mensual:")

if edad_str.isdigit() == True:
    if antiguedad_str.isdigit() == True:
        if ingreso_str.isdigit() == True:
             edad = int(edad_str)

             if edad <= 18:
                 print("Eres menor de edad")
             else:
                 antiguedad = int(antiguedad_str)
                 ingreso = float(ingreso_str)

                 if antiguedad < 3:
                    if ingreso < 4000:
                        print("Prestamo denegado por falta de Ingreso")
                 else:
                     if ingreso < 2500:

        else:
           print("No ingreso un ingreso")
    else:
        print("No ingreso una antiguedad")    
else:
    print("No ingreso una edad")