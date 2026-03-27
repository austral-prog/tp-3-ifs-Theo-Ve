from traceback import print_exc


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre_completo = input("Ingrese su nombre completo: ") #Inputs para que el usuario ingrese nombre, email y 3 notas
    email = input("Ingrese su email: ")
    nota1 = input("Ingrese una nota: ")
    nota2 = input("Ingrese una nota: ")
    nota3 = input("Ingrese una nota: ")

    print("========================") #Encabezado decorativo
    print("    FICHA DEL ALUMNO")
    print("========================")

    nombre_limpio = nombre_completo.strip()

    print(f"Nombre: {nombre_limpio.title()}") #Nombre limpio: sin espacios extra y con formato título

    print(f"Email: {email.lower()}") #Email en minúsculas

    print(f"Caracteres en nombre: {len(nombre_limpio)}") #Cantidad de caracteres del nombre

    iniciales = nombre_limpio.find(" ") #iniciales del nombre y apellido
    print(f"Iniciales: {(nombre_limpio[0] + nombre_limpio[iniciales + 1]).upper()}")

    nombre = nombre_limpio[:iniciales].lower() #apellido.nombre en minuscula
    apellido = nombre_limpio[iniciales + 1:].lower()
    print(f"Usuario: {apellido}.{nombre}")

    print(f"Email valido: {"@" in email}") #Verifica si el email contiene @

    dom = (email.find("@")) #Extraer el dominio del email
    print(f"Dominio: {email[dom + 1:]}".lower())

    print(f"Nombre para archivo: {nombre_limpio.title().replace(' ', '_')}") #Nombre con guion bajo en vez de espacio

    print(f"Cantidad de a: {nombre_limpio.lower().count("a")}") #Cuenta las 'a' en el nombre

    print(f"Codigo secreto: {nombre_limpio[-1::-1]}".upper()) #nombre invertido en mayúsculas

    print(f"Nota 1: {nota1}") #las 3 notas
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    n1 = int(nota1) #transformo el string en numeros
    n2 = int(nota2)
    n3 = int(nota3)

    suma = n1 + n2 + n3
    print(f"Suma: {suma}") #suma de las 3 notas

    print(f"Promedio: {suma/3}") #promedio de las 3 notas

    print(f"Promedio entero: {int(suma/3)}") #promedio entero de las 3 notas

    print("=" * 24) #Cierre decorativo


ficha()



