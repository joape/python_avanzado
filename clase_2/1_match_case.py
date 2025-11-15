numero =  int(input("Ingresa un numero del 1 al 3: "))

match numero:
    case 1:
        print("El numero es 1")
    case 2:
        print("El numero es 2")
    case 3:
        print("El numero es 3")
    case _:
        print("Es otro numero")