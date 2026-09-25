def estructuras():
    # LIFO
    pila = []

    pila.append("Juan")
    pila.append("Pedro")
    pila.append("Carlos")

    print("LIFO:")
    while pila:
        print(pila.pop())

    # FIFO
    fila = []

    fila.append("Juan")
    fila.append("Pedro")
    fila.append("Carlos")

    print("\nFIFO:")
    while fila:
        print(fila.pop(0))


estructuras()