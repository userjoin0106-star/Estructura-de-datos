def multiplicar_matrices():
    print("Matriz A")
    a = []
    for i in range(2):
        fila = []
        for j in range(2):
            numero = int(input(f"Digite A[{i}][{j}]: "))
            fila.append(numero)
        a.append(fila)

    print("\nMatriz B")
    b = []
    for i in range(2):
        fila = []
        for j in range(2):
            numero = int(input(f"Digite B[{i}][{j}]: "))
            fila.append(numero)
        b.append(fila)

    resultado = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultado[i][j] += a[i][k] * b[k][j]

    print("\nResultado:")
    for fila in resultado:
        print(fila)


multiplicar_matrices()