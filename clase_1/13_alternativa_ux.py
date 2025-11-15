edad = int(input("Edad: "))

if edad >= 18:
    ingreso_mensual = float(input("Ingreso mensual: "))
    if ingreso_mensual >= 4000:
        print("Crédito aprobado")
    else:
        antiguedad_laboral = int(input("Antigüedad laboral (años): "))
        if antiguedad_laboral >= 3 and ingreso_mensual > 2500:
            print("Crédito aprobado")
        else:
            print("Crédito no aprobado")
else:
    print("Crédito no aprobado")
