def ejercicio1 ():
    Nombre = input("ingrese su nombre: ") 
    Edad = int(input("ingrese la edad: "))
    Programa = input("Ingrese el programa: ")
    Promedio = float(input("lingrese la nota: "))
    print(Nombre,Edad,Programa,Promedio)
    print(type(Nombre),type(Edad),type(Programa),type(Promedio))
    print (F"El estudiante {Nombre} tiene {Edad} años, cursa el programa {Programa} y tiene un promedio de {Promedio}")
    

ejercicio1 ()