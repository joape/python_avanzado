"""
A partir de la siguiente lista, iterar y mostrar por pantalla los nombres
de ciudades que tengan más de una palabra
"""

capitales_latinoamerica = [
    ("Argentina", "Buenos Aires"),
    ("Bolivia", "Sucre"),
    ("Brasil", "Brasilia"),
    ("Chile", "Santiago de Chile"),
    ("Colombia", "Bogotá"),
    ("Costa Rica", "San José"),
    ("Cuba", "La Habana"),
    ("Ecuador", "Quito"),
    ("El Salvador", "San Salvador"),
    ("Guatemala", "Ciudad de Guatemala"),
    ("Honduras", "Tegucigalpa"),
    ("México", "Ciudad de México"),
    ("Nicaragua", "Managua"),
    ("Panamá", "Ciudad de Panamá"),
    ("Paraguay", "Asunción"),
    ("Perú", "Lima"),
    ("República Dominicana", "Santo Domingo"),
    ("Uruguay", "Montevideo"),
    ("Venezuela", "Caracas"),
]

print(f"{'País':<25}{'Ciudad':<25}")
print("-" * 50)
for pais, ciudad in capitales_latinoamerica:
    if len(ciudad.split()) > 1:
        print(f"{pais:<25}{ciudad:<25}")