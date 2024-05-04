"""
Trabajo grupal matrices

Consigna: Desarollar un programa capaz de multiplicar dos matrices ingresadas por el usuario. Validar las dimensiones de cada una para que sea consistente con el procedimiento

Integrantes del grupo: Teo Leone, Sebastían Hereñu Amaral, Rodrigo Fleitas, Nicolás Doyhenart
"""

def ingresar_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(
                input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))
            fila += [valor]
        matriz += [fila]
    return matriz


##########################################################################################################


def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("No se pueden multiplicar las matrices. Las dimensiones no son consistentes.")
        return None
    resultado = []

    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila += [suma]
        resultado += [fila]
    return resultado


##########################################################################################################


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

matriz1 = ingresar_matriz()
matriz2 = ingresar_matriz()

print("\nMatriz 1:")
mostrar_matriz(matriz1)
print("\nMatriz 2:")
mostrar_matriz(matriz2)

resultado = multiplicar_matrices(matriz1, matriz2)
if resultado:
    print("\nResultado de la multiplicación:")
    mostrar_matriz(resultado)
