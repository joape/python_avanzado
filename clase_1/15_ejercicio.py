"""
Refactorizar usando else (no usar elif) para que aparezca
un solo mensaje según la edad
"""

edad = int(input("Edad: "))

if edad < 13:
    print("Eres un niño")
else:
    if edad < 18:
        print("Eres un adolescente")
    else:
        if edad < 65:
            print("Eres un adulto")
        else:
            if edad < 75:
                print("Eres un adulto mayor")
            else:
                if edad < 120:
                    print("Eres un anciano")
