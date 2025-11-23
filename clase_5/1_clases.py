class Ciudad:
    def __init__(self, nombre, poblacion):  # método constructor
        print("Se está creando una ciudad...")
        self.nombre = nombre  # atributo / variable de instancia
        self.poblacion = poblacion  # atributo / variable de instancia

mendoza = Ciudad(nombre="Mendoza", poblacion=1_150_000)  # objeto de la clase Ciudad
cordoba = Ciudad(nombre="Córdoba", poblacion=1_300_000)  # instancia de la clase Ciudad
print(mendoza.nombre, mendoza.poblacion)
print(cordoba.nombre, cordoba.poblacion)
print(
    f"La ciudad de {mendoza.nombre} tiene una población de {mendoza.poblacion} habitantes."
)
print(
    f"La ciudad de {cordoba.nombre} tiene una población de {cordoba.poblacion} habitantes."
)