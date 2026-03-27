def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Ingresar nombre: ") #el usuario ingresa su nombre y luego se establece una variable del nombre en minuscula
    nombre = nombre.lower()

    print(f"Contiene a: {'a' in nombre}") #se buscan las vocales en el nombre
    print(f"Contiene e: {'e' in nombre}")
    print(f"Contiene i: {'i' in nombre}")
    print(f"Contiene o: {'o' in nombre}")
    print(f"Contiene u: {'u' in nombre}")

check_vowels()
