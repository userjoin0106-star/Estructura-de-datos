def ejercicio1():

    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    # Crear las tablas como vectores
    tabla1 = []
    tabla2 = []

    # Generar la primera tabla
    for i in range(1, 11):
        tabla1.append(numero1 * i)

    # Generar la segunda tabla
    for i in range(1, 11):
        tabla2.append(numero2 * i)

    # Multiplicar los dos vectores
    resultado = []

    for i in range(10):
        resultado.append(tabla1[i] * tabla2[i])

    # Mostrar la primera tabla
    print("\nTABLA DEL", numero1)

    for i in range(10):
        print(numero1, "x", i + 1, "=", tabla1[i])

    # Mostrar la segunda tabla
    print("\nTABLA DEL", numero2)

    for i in range(10):
        print(numero2, "x", i + 1, "=", tabla2[i])

    # Mostrar el resultado
    print("\nRESULTADO DE MULTIPLICAR LAS DOS TABLAS")

    for i in range(10):
        print(tabla1[i], "x", tabla2[i], "=", resultado[i])


ejercicio1()