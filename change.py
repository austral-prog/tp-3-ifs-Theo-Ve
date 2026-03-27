def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass


    gasto = float(input("Ingrese el gasto: "))  #se solicita el gasto y el dinero recibido al usuario
    dinero_recibido = int(input("ingrese el dinero recibido: "))

    print("Ingresar gasto:")  #se imprime lo ingresado
    print(gasto)

    print("Dinero recibido")
    print(dinero_recibido)

    print("")
    print("Vuelto")
    print("")

    vuelto = dinero_recibido - gasto  #se establecen el dinero restante en pesos y centavos
    pesos = int(vuelto)
    centavos = vuelto - pesos

    print("Pesos:")  #se imprime el dinero restante
    print(pesos)
    print("Centavos:")
    print(round(centavos * 100))

change()