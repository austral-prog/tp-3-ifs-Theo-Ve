def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos
    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)
    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento
    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final
    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """
    pass

    #precio = float(input("Ingrese el precio del producto: ")) # Lee el precio unitario (decimal)
    #cant = int(input("Ingrese la cantidad de producrtos que desea comprar: ")) # Lee la cantidad (entero)

    precio = float(input())
    cant = int(input())

    print(f"Subtotal: {precio * cant}") # Muestra el subtotal directamente

    subtotal = precio * cant # Calcula y guarda el subtotal

    # Porcentajes de descuento posibles
    desc1 = 20.0
    desc2 = 10.0
    desc3 = 0.0

    # Determina qué porcentaje de descuento aplicar según la cantidad
    if cant >= 10:
        print(f"Descuento aplicado: {desc1}%")
    elif 5 <= cant <= 9:
        print(f"Descuento aplicado: {desc2}%")
    else:
        print(f"Descuento aplicado: {desc3}%")

    # Calcula y muestra el monto del descuento (en dinero)
    if cant >= 10:
        print(f"Monto del descuento: {desc1 * subtotal / 100}")
        desc_dsp = desc1 # Guarda el descuento aplicado
    elif 5 <= cant <= 9:
        print(f"Monto del descuento: {desc2 * subtotal / 100}")
        desc_dsp = desc2
    else:
        print(f"Monto del descuento: {desc3}")
        desc_dsp = desc3

    descuento = subtotal * desc_dsp / 100 # Calcula el descuento en dinero

    print(f"Total final: {subtotal - descuento}") # Calcula y muestra el total final

#discount()