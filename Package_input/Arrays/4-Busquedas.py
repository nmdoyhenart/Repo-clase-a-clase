lista = [4, 9, 8 , -9, -7, -3]

# for i in range(len(lista)):
#     if lista[i] < 0:
#         posicion = i
                                    
# if posicion != -1:
#     print("Hay un negativo")
# else:
#     print("No hay un negativo")

contador_negativos = 0
for i in range(len(lista)):
    if lista[i] < 0:
        contador_negativos += 1

if contador_negativos > 0:
    print("Hay un negativo")
else:
    print("No hay un negativo")
