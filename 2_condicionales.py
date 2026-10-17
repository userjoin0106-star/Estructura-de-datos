
def ejercicio2 ():
    nota = float(input("Ingrese la nota: "))
    if nota >= 3 and nota <= 5:
        print("Aprobado")
    else:
        print ("No aprobado")
    if nota < 0 or nota > 5:
        print ("Nota invalida")

ejercicio2 ()