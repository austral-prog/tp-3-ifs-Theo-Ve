def age_check():
    """
    Ejercicio 3 - Verificar Mayoría de Edad

    Leer una edad y un límite de edad mediante input(). Verificar que ambos números sean
    válidos (positivos), y luego determinar si la persona es mayor de edad comparando
    con el límite ingresado.

    Si alguno de los números es negativo o cero, imprimir "Entrada invalida".

    Ejemplo:
        Para las entradas "20" y "18", la salida esperada es:
        Eres mayor de edad

        Para las entradas "16" y "18", la salida esperada es:
        Eres menor de edad

        Para las entradas "-5" y "18", la salida esperada es:
        Entrada invalida
    """
    pass

    edad = int(input("Ingrese su edad: ")) # Lee la edad de la persona y el limite de edad
    lim = int(input("Ingrese una edad maxima: "))

    if edad <= 0: # Verifica si la edad es inválida (menor o igual a 0)
        print("Entrada invalida")
    elif edad >= lim: # Compara si la edad es mayor o igual al límite
        print("Eres mayor de edad")
    elif edad < lim: # Caso contrario: es menor que el límite
        print("Eres menor de edad")

age_check()


