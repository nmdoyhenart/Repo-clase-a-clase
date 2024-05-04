"""
LISTAS + FUNCIONES
"""

def mostar_lista(lista: list, ilogico: int)-> bool:
    exito = False
    if type(lista) == list and type(ilogico) == int:
        exito = True
        for i in range(len(lista)):
            if lista[i] != ilogico:  
                print(f"{i + 1} -> {lista[i]}")
    return exito

def cargar_valor(lista, posicion, valor, ilogico)-> bool:
    exito = False
    if lista[posicion] == ilogico:
        lista[posicion] = valor
        exito = True
    
    return exito

#####################################################

lista = [-1] * 5

bandera_seguir = True

while True:
    posicion = int(input("Ingrese posición: "))
    while posicion < 1 or posicion > len(lista):
        posicion = int(input("Reingrese posición: "))

    numero = int(input("Ingrese un numero: "))

    lista[posicion - 1] = numero

    seguir = input("Desea continuar? si/no: ")
    if seguir != "si":
        break

if not mostar_lista(lista, -1):
    print("Hubo un error al intentar mostrar la lista")

