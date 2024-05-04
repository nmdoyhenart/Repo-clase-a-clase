import random
for L in range(0,15):
    num_legajo = random.randint((100000,999999))


C = [[1,2,3,4,5],
     [9,7,10,18,13],
     [6,32,19,44,8]]

for i in range(len(C)):
    for j in range(len(C[i])):
        print(C[i][j])

C = [[1,9,6],
     [8,7,10,18,13],
     [12,32,19,44,8]]

for i in range(len(C)):
    linea = C[i]
    print(linea)
    numero = int(input("Ingrese su linea: "))
    if numero == 1 or numero == 9 or numero == 6:
        linea = numero
    else:
        numero = int(input("Linea erronea, elija entre las lineas 1,9 o 6: "))
        print(linea)

    #for j in range(len(C[i])):
       #print(C[i][j])
    
