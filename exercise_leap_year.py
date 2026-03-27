def leap_year():
    """
    Ejercicio 11 (Desafío) - Año Bisiesto

    Leer un año mediante input(). Determinar si es un año bisiesto e imprimir el resultado.
    Un año es bisiesto si:
    - Es divisible por 4, Y
    - NO es divisible por 100, O es divisible por 400

    Ejemplo:
        Para la entrada "2000", la salida esperada es:
        El año 2000 es bisiesto

        Para la entrada "2001", la salida esperada es:
        El año 2001 no es bisiesto

        Para la entrada "1700", la salida esperada es:
        El año 1700 no es bisiesto
    """
    pass

    #ano = int(input("Ingrese un año: ")) # Lee el año como número entero
    ano = int(input())

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0: # Verifica si el año es bisiesto: si es divisible por 4 y no por 100, o si es divisible por 400
        print(f"El año {ano} es bisiesto")
    else:
        print(f"El año {ano} no es bisiesto")

#leap_year()