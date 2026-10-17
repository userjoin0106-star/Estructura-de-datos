class Banco:

    def __init__(self):
        self.fila = []
        self.cantidad = 0

    def ingresar_clientes(self):
        self.cantidad = int(input("Cuantos clientes entraron: "))

        i = 0
        while i < self.cantidad:
            nombre = input("Ingrese el nombre del cliente: ")

            while not nombre.isalpha():
                print("Error: solo se permiten letras")
                nombre = input("Ingrese el nombre del cliente: ")

            self.fila.append(nombre)
            i = i + 1

    def vacio(self):
        return len(self.fila) == 0

    def atender(self):
        while not self.vacio():
            cliente = self.fila.pop(0)
            print("Caja 1 atendio a:", cliente)

            if not self.vacio():
                print("Todavia quedan personas por atender.")
            else:
                print("Ya no quedan personas por atender.")


banco = Banco()

banco.ingresar_clientes()
banco.atender()