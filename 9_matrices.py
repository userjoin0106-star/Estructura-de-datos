def ejercicio9():

    cantidad_asignaturas = int(input("¿Cuántas asignaturas desea ingresar?: "))

    asignaturas = []

    for i in range(cantidad_asignaturas):

        asignatura = input("Ingrese el nombre de la asignatura " + str(i + 1) + ": ")

        asignaturas.append(asignatura)

    cantidad_estudiantes = int(input("¿Cuántos estudiantes desea ingresar?: "))

    estudiantes = []

    notas = []

    for i in range(cantidad_estudiantes):

        nombre = input("Ingrese el nombre del estudiante " + str(i + 1) + ": ")

        estudiantes.append(nombre)

        notas_estudiante = []

        for j in range(cantidad_asignaturas):

            nota = float(input("Ingrese la nota de " + asignaturas[j] + ": "))

            notas_estudiante.append(nota)

        notas.append(notas_estudiante)

    print("==============================")
    print("       NOTAS DEL GRUPO")
    print("==============================")

    for i in range(cantidad_estudiantes):

        print("Estudiante:", estudiantes[i])

        for j in range(cantidad_asignaturas):

            print(asignaturas[j], ":", notas[i][j])

        print("------------------------------")

    print("PROMEDIO DE CADA ESTUDIANTE")

    for i in range(cantidad_estudiantes):

        suma = 0

        for j in range(cantidad_asignaturas):

            suma = suma + notas[i][j]

        promedio = suma / cantidad_asignaturas

        print(estudiantes[i], ":", promedio)

    print("------------------------------")
    print("PROMEDIO DE CADA ASIGNATURA")

    for j in range(cantidad_asignaturas):

        suma = 0

        for i in range(cantidad_estudiantes):

            suma = suma + notas[i][j]

        promedio = suma / cantidad_estudiantes

        print(asignaturas[j], ":", promedio)

    mayor = notas[0][0]
    menor = notas[0][0]

    for i in range(cantidad_estudiantes):

        for j in range(cantidad_asignaturas):

            if notas[i][j] > mayor:
                mayor = notas[i][j]

            if notas[i][j] < menor:
                menor = notas[i][j]

    print("------------------------------")
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)


ejercicio9()