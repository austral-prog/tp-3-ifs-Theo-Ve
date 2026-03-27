def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    nombre = input("Di tu nombre: ")   #se crea un input para que el usuario ingrese su nombre y apellido
    apellido = input("Di tu apellido: ")

    print((nombre.lower() + " " + apellido.lower()))  #se imprime el nombre y apellido del usuario en distintos formatos
    print((nombre.title() + " " + apellido.title()))
    print((nombre.upper() + " " + apellido.upper()))
    print("\t" + nombre.lower() + " " + apellido.lower())

names()