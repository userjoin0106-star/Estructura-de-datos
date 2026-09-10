def ejercicio6():

    estudiantes = []

    cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))

    for i in range(cantidad):

        nombre = input("Ingrese el nombre del estudiante " + str(i + 1) + ": ")

        estudiantes.append(nombre)

    while True:

        print("==============================")
        print("     SISTEMA DE ESTUDIANTES")
        print("==============================")
        print("1. Mostrar estudiantes")
        print("2. Mostrar primer estudiante")
        print("3. Mostrar último estudiante")
        print("4. Mostrar cantidad de estudiantes")
        print("5. Agregar estudiante")
        print("6. Eliminar estudiante")
        print("7. Buscar estudiante")
        print("8. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            print("Lista de estudiantes:")

            for estudiante in estudiantes:
                print(estudiante)

        elif opcion == 2:

            if len(estudiantes) > 0:
                print("Primer estudiante:", estudiantes[0])
            else:
                print("No hay estudiantes")

        elif opcion == 3:

            if len(estudiantes) > 0:
                print("Último estudiante:", estudiantes[-1])
            else:
                print("No hay estudiantes")

        elif opcion == 4:

            print("Cantidad de estudiantes:", len(estudiantes))

        elif opcion == 5:

            nombre = input("Ingrese el nombre del nuevo estudiante: ")

            estudiantes.append(nombre)

            print("Estudiante agregado correctamente")

        elif opcion == 6:

            nombre = input("Ingrese el nombre del estudiante que desea eliminar: ")

            if nombre in estudiantes:

                estudiantes.remove(nombre)

                print("Estudiante eliminado correctamente")

            else:

                print("El estudiante no existe")

        elif opcion == 7:

            nombre = input("Ingrese el nombre del estudiante que desea buscar: ")

            if nombre in estudiantes:

                print("Estudiante encontrado")

            else:

                print("Estudiante no encontrado")

        elif opcion == 8:

            print("Programa terminado")
            break

        else:

            print("Opción inválida")


ejercicio6()