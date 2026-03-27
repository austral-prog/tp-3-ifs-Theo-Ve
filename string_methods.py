def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    print(f"Strip: {nombre.strip()}") #se imprime el nombre sin espacios

    print(f"Lstrip: {nombre.lstrip()}") #se imprime el nombre sin espacios a la izquierda

    print(f"Rstrip: {nombre.rstrip()}") #se imprime el nombre sin espacion a la derecha

    print(f"Upper: {frase.upper()}") #se imprime la frase en mayusculas

    print(f"Lower: {frase.lower()}") #se imprime la frase en minusculas

    print(f"Title: {frase.title()}") #se imprime la frase con mayuscula en la primera letra de cada palabra

    print(f"Find: {frase.find("gran")}") #se imprime en que numero de la frase aparece "gran"

    print(f"Replace: {frase.replace("programacion", "desarrollo")}") #se imprime la frase reemplazando "programacion" por "desarrollo"

    print(f"Count: {frase.count("a")}") #se imprime la cantidad de veces que aparece "a"

    print(f"Contiene Python: {"Python" in frase}") #se imprime si aparece la palabra "Python" en la frase o no

    print(f"Contiene Java: {"Java" in frase}") #se imprime si aparece la palabra "Java" en la frase o no

    print(f"Slice: {frase[0:6]}") #se imprime la seccion 0 a 6 en la frase

    p = "Python" #se establece una variable

    print(f"Paso: {p[::2]}") #se imprime la variable tomando 1 letra cada 2

    print(f"Reverso: {p[::-1]}") #se imprime la variable al reves

    print(f"Formato: {nombre.strip()} sabe Python") #se imprime el nombre con una frase

    l1 = multilinea[0:7] #se imprimen las palabras en la multilinea
    print(l1)
    l2 = multilinea[12:19]
    print(l2)
    l3 = multilinea[24:31]
    print(l3)

string_methods()