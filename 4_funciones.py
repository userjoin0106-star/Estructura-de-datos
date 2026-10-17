def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def ejercicio4():

    while True:

        print("=========================")
        print("       CALCULADORA")
        print("=========================")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = int(input("Seleccione: "))

        if opcion == 5:
            print("Programa terminado")
            break

        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("Resultado:", sumar(numero1, numero2))

        elif opcion == 2:
            print("Resultado:", restar(numero1, numero2))

        elif opcion == 3:
            print("Resultado:", multiplicar(numero1, numero2))

        elif opcion == 4:
            if numero2 != 0:
                print("Resultado:", dividir(numero1, numero2))
            else:
                print("No se puede dividir entre cero")

        else:
            print("Opción inválida")


ejercicio4()