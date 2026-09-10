def ejercicio3():

    while True:

        print("==============================")
        print("       MENU DE NUMEROS")
        print("==============================")
        print("1. Mostrar números del 1 al 100")
        print("2. Mostrar números pares")
        print("3. Mostrar números impares")
        print("4. Mostrar múltiplos de 5")
        print("5. Mostrar la suma del 1 al 100")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            for numero in range(1, 101):
                print(numero)

        elif opcion == 2:

            for numero in range(1, 101):
                if numero % 2 == 0:
                    print(numero)

        elif opcion == 3:

            for numero in range(1, 101):
                if numero % 2 != 0:
                    print(numero)

        elif opcion == 4:

            for numero in range(1, 101):
                if numero % 5 == 0:
                    print(numero)

        elif opcion == 5:

            suma = 0

            for numero in range(1, 101):
                suma = suma + numero

            print("La suma de los números del 1 al 100 es:", suma)

        elif opcion == 6:

            print("Programa terminado")
            break

        else:

            print("Opción inválida")


ejercicio3()