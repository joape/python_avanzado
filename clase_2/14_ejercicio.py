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

for pais, ciudad in capitales_latinoamerica:
    if len(ciudad.split()) > 1:  # Si la ciudad tiene más de una palabra
        print(ciudad)