def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass

    contra = input("Cree su conraseña: ") # Pide la contraseña al usuario

    long_contr = len(contra) # Calcula la longitud de la contraseña

    if long_contr >= 8: # Verifica si la contraseña tiene al menos 8 caracteres
        if "0" in contra or "1" in contra or "2" in contra or "3" in contra or "4" in contra or "5" in contra or "6" in contra or "7" in contra or "8" in contra or "9" in contra:
            print("Contraseña valida") # Verifica si contiene al menos un número (0-9)
        else:
            print("Contraseña invalida") # No tiene números
    else:
        print("Contraseña muy corta") # No cumple con la longitud mínima

#password()