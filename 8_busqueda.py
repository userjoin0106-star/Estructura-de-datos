def ejercicio8():

    productos = [
        "Teclado",
        "Mouse",
        "Monitor",
        "Impresora",
        "Memoria RAM",
        "Disco SSD"
    ]

    producto = input("Ingrese el producto que desea buscar: ")

    encontrado = False

    for elemento in productos:

        if elemento.lower() == producto.lower(): #
            encontrado = True

    if encontrado:
        print("Producto encontrado")
    else:
        print("Producto no encontrado")


ejercicio8()