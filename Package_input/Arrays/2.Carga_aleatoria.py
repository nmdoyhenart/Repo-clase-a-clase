"""
CARGA ALEATORIA
"""
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

for i in range(len(lista)):
    if lista[i] != -1:  
        print(f"{i + 1} -> {lista[i]}")

