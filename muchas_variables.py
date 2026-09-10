def ejercicio5():

    cantidad = int(input("¿Cuántas notas desea ingresar?: "))

    notas = []

    for i in range(cantidad):

        nota = float(input("Ingrese la nota " + str(i + 1) + ": "))

        notas.append(nota)

    suma = 0
    mayor = notas[0]
    menor = notas[0]
    aprobados = 0

    for nota in notas:

        suma = suma + nota

        if nota > mayor:
            mayor = nota

        if nota < menor:
            menor = nota

        if nota >= 3:
            aprobados = aprobados + 1

    promedio = suma / cantidad

    print("==============================")
    print("       INFORMACION DE NOTAS")
    print("==============================")
    print("Cantidad de notas:", cantidad)
    print("Promedio:", promedio)
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)
    print("Cantidad de aprobados:", aprobados)


ejercicio5()