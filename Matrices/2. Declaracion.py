matriz = [[0] * 3 for _ in range(4)]

for i in range(len(matriz)): # Filas
    for j in range(len(matriz[i])): # Columnas
        print(f"{matriz[i][j]}", end = " ")
    print("")