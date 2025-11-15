def sumar(*args: int | float) -> None:
    print(type(args))
    print(args)
    print(sum(args))


sumar(10, 2, 1000, 1, -0.3)
