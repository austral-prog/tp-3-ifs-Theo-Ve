def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass

    base = int(input("Ingresar la base del rectangulo: ")) #el ususario ingresa la bsa y altura de un rectangulo
    altura = int(input("Ingresar la altura del rectangulo: "))

    print(f"Base: {base}") #la base y altura se imprime
    print(f"Altura: {altura}")

    area = base * altura #se calcula el area y perimetro
    perimetro = base * 2 + altura * 2

    print(f"Area: {area}") #se imprime el area y perimetro
    print(f"Perimetro: {perimetro}")

rectangle()
