print("hola", "adiós", sep=" - ", end="***")
print("hola", "adiós", sep=" - ", end="\n")
print()

import time

texto = "Python es genial!"

for x in texto:
    print(x, end="\r")
    time.sleep(0.4)
