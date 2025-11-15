"""
Refactorizar usando else (no usar elif) para que aparezca
un solo mensaje según la edad
"""

edad = int(input("Edad: "))

if edad < 0 or edad >= 120:
    print("Edad inválida")
elif edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
elif edad < 75:
    print("Eres un adulto mayor")
elif edad < 120:
    print("Eres anciano")
