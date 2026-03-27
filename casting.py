def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input("Ingrese el precio: ")) #el usuario ingresa los datos
    descuento = float(input("Ingrese el descuento: "))
    cantidad = int(input("Ingrese la cantidad: "))

    print(f"Precio: {precio}")#se imprime lo escrito

    print(f"Descuento: {descuento}")

    precio_reducido = float(precio - descuento)
    print(f"Precio con descuento: {precio_reducido}")

    total = float(precio_reducido * cantidad)
    print(f"Total: {total}")

casting()




