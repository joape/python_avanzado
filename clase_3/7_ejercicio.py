"""
crear la lista gente como una lista por comprensión a partir del siguiente código
nombres = ["Daniel", "Natalia", "Franco"]
numeros = [55, 50, 45]

gente: list[tuple[str, int]] = []

for nombre in nombres:
    for n in numeros:
        gente.append((nombre, n))

print(gente)
"""

nombres = ["Daniel", "Natalia", "Franco"]
numeros = [55, 50, 45]

# gente: list[tuple[str, int]] = []

# for nombre in nombres:
#     for n in numeros:
#         gente.append((nombre, n))

gente = [(nombre, n) for nombre in nombres for n in numeros]

print(gente)
