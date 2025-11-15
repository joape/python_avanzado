# Las variables siguen el estilo snake_case

edad_str = input("Edad: ")

if edad_str.isdecimal():
    edad = int(edad_str)  # castear / parsear
    if edad >= 18:
        print("Eres mayor edad")
    else:
        print("Eres menor de edad")
else:
    print("No has ingresado un número")
