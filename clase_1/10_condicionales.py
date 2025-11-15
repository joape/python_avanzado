password = "adminpass"

respuesta = input("Contraseña: ")

if respuesta == password:  # lo que está a la derecha de if se llama "expresión"
    print("✅ Acceso correcto")
else:
    print("❌ Acceso denegado")
