matriz = [
    [4,9,6],
    [7,9,3],
    [1,2,3],
    [7,2,8]
]

F = len(matriz)
C = len(matriz[0])

matriz_resultado = [[0]*C for _ in range(F)]

escalar = 5

for i in range(F):
    for j in range(C):
        matriz_resultado[i][j] = escalar * matriz[i][j]

for i in range(F): #   -> 2
    for j in range(C): #   -> 1
        print(f"{matriz_resultado[i][j]:<5}", end = " ")
    print("")

