#comparacion de letras palindromas con lifo y fifo
class Palindromo:

    def __init__(self):
        self.fila = []
        self.pila = []

    def ingresar_palabra(self):
        palabra = input("Ingrese una palabra: ").lower()

        for letra in palabra:
            self.fila.append(letra)
            self.pila.append(letra)

    def vacio(self):
        return len(self.fila) == 0

    def comparar(self):
        while not self.vacio():

            letra_fifo = self.fila.pop(0)
            letra_lifo = self.pila.pop()

            if letra_fifo != letra_lifo:
                print("La palabra no es palíndroma.")
                return

        print("La palabra es palíndroma.")


palabra = Palindromo()

palabra.ingresar_palabra()
palabra.comparar()






#primera forma de recorrer 
i=0
#while i < len(l)
#print(l(i))
#i += 1

#segunda forma
#for i in range(L)
    #print(i)

#tercera forma para recorrer
# for i en L (longitud de vector)
    #print (i)

