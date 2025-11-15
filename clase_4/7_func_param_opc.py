def dar_pasos(pasos: int = 0):
    if not isinstance(pasos, int):
        # raise ValueError("Debes pasar un entero")
        print("Debes pasar un entero")
        return
    pasos = int(pasos)
    if pasos:
        print(f"Estoy dando {pasos} pasos")
    else:
        print("No estoy dando pasos")


dar_pasos(100)
dar_pasos()
dar_pasos(1.4)
