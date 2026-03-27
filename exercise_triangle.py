def triangle():
    """
    Ejercicio 8 - Validar Triángulo

    Leer tres números que representan los lados de un triángulo mediante input().
    Verificar si pueden formar un triángulo válido e imprimir el resultado.
    Un triángulo es válido si la suma de dos lados cualesquiera es estrictamente mayor
    que el tercer lado (desigualdad triangular). Si la suma es igual, forman una línea
    recta, no un triángulo.

    Ejemplo:
        Para las entradas "3", "4" y "5", la salida esperada es:
        Los lados forman un triangulo valido

        Para las entradas "1", "2" y "5", la salida esperada es:
        Los lados no forman un triangulo valido
    """
    pass

    lado1 = float(input("Ingrese la longitud de un lado de un triangulo: ")) # Lee los lados de un triangulo
    lado2 = float(input("Ingrese la longitud de un lado de un triangulo: "))
    lado3 = float(input("Ingrese la longitud de un lado de un triangulo: "))

    if lado1 + lado2 > lado3: # Verifica si la suma de 2 lados es mayor que el 3
        if lado1 + lado3 > lado2:
            if lado2 + lado3 > lado1:
                print("Los lados forman un triangulo valido") # Si se cumplen las tres condiciones, es un triángulo válido
            else:
                print("Los lados no forman un triangulo valido") # Se imprime esto si alguna suma no es superior al 3 lado
        else:
            print("Los lados no forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")


#triangle()
