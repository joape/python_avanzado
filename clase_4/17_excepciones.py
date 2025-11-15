"""
Manejo de excepciones

try:
    # código que puede lanzar una excepción
except:
    # código que se ejecuta si se lanza una excepción
else:
    # (opcional) código que se ejecuta si no se lanza una excepción
finally:
    # (opcional) código que se ejecuta siempre
"""

try:
    numero_1 = int(input("Ingresa un número: "))
    numero_2 = int(input("Ingresa otro número: "))
    division = numero_1 / numero_2
except ValueError:
    print("❌ Se debe ingresar un número")
except ZeroDivisionError:
    print("❌ No se puede dividir por cero")
except Exception as mensaje:
    print("❌ Error inesperado:", type(mensaje))
except KeyboardInterrupt:
    print("\nEl usuario ha salido.")
else:
    print(division)
# finally:
#     print("..siempre se ejecuta..")
