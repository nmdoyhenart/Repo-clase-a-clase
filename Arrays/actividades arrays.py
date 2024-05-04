"""
Nombre: Nicolás
Apellido: Doyhenart

Escribir una función que reciba como parámetros una lista de enteros y muestre 
la/las posiciones en donde se encuentra el valor máximo hallado.
"""
def valores_max(lista : list):
    num_max = 0
    posiciones_max = []
    bandera = True
    for i in range(len(lista)):   
        if bandera == True:
            num_max = lista[i]
            bandera = False
        else:
            if num_max < lista[i]:
                num_max = lista[i]
    
    for a in range(len(lista)):
        if lista[a] == num_max:
            posiciones_max.append(a)
    return posiciones_max

lista = [5, 10, 2, 10, 2, 10]
posiciones = valores_max(lista)
print(posiciones)


    