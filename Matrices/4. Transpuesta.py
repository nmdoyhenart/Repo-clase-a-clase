matriz = [
    [40,9,6],
    [700, 90, 3],
    [7,9000,-3],
    [7, -90, 3]
]

for j in range(len(matriz[0])): #   -> 2
    for i in range(len(matriz)): #   -> 1
        print(f"{matriz[i][j]:<5}", end = " ")
    print("")
