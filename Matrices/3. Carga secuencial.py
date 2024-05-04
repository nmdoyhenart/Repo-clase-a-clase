matriz = [[0] * 3 for _ in range(2)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Ingrese un numero: "))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]}", end = " ")
    print("")