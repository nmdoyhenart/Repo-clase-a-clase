"""
Nombre: Nicolás
Apellido: Doyhenart
TP Menú-Arrays-Funciones 26/4

-Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
1-Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
2-Mostrar la cantidad de números positivos y negativos.
3-Mostrar la sumatoria de los números pares.
4-Informar el mayor de los números impares.
5-Listar todos los números ingresados.
6-Listar todos los números pares.
7-Listar los números de las posiciones impares.  
8-Salir
"""
from os import system
def ingreso_numeros(minimo: int, maximo: int)-> int:
        numero = int(input("Ingrese un numero: "))
        if numero > maximo or numero < minimo:
            numero = int(input("Ingrese un valor valido: "))
        return numero

num_positivos = 0
num_negativos = 0
bandera_ingreso = False
bandera_seguir = True
lista_ingresos = []

while bandera_seguir:
    opcion = int(input("""1-Ingresar 10 numeros\n 2-Mostrar cantidad de numeros positivos y negativos\n 3-Sumatoria de numeros pares\n 4-Mayor de los numeros pares\n 5-Todos los numeros ingresados\n 6-Todos los numeros pares\n 7-Numeros de las posiciones impares\n 8-Salir\n Elija una opcion: """))

    match opcion:
            case 1:
                for i in range(10):
                    numeros = ingreso_numeros(-1000, 1000)
                    lista_ingresos.append(numeros)
                    bandera_ingreso = True
            case 2:
                if bandera_ingreso == True:
                    for i in range(len(lista_ingresos)):
                        if lista_ingresos[i] > 0:
                            num_positivos += 1
                        else:
                            num_negativos += 1
                        print(f"Los numeros positivos ingresados son: {num_positivos} y los negativos son: {num_negativos}")
                else:
                    print("Ingrese numeros para ver esta opcion")
                    break
            case 3:
                suma_numeros_pares = 0
                if bandera_ingreso == True:
                    for i in range (len(lista_ingresos)):
                        if (lista_ingresos[i] % 2) == 0:
                            suma_numeros_pares += lista_ingresos[i]
                            print(f"La sumatoria de todos los numeros ingresados pares es {suma_numeros_pares}.")
                else:
                    print("Ingrese numeros para ver esta opcion")
                    break
            case 4:
                impares_mayor = 0
                if bandera_ingreso == True:
                    if (lista_ingresos[i] % 2) != 0 or lista_ingresos[i] > impares_mayor:
                        impares_mayor = lista_ingresos[i]
                        print(f"El mayor impar ingresado es: {impares_mayor}")
                else:
                    print("Ingrese numeros para ver esta opcion")
                    break
            case 5:
                if bandera_ingreso == True:
                    for i in range(len(lista_ingresos)):
                        print(f"Lista de numeros ingresados: {lista_ingresos}")
                else:
                    print("Ingrese numeros para ver esta opcion")
                    break
            case 6:
                lista_pares = []
                if bandera_ingreso == True:
                    for i in range (len(lista_ingresos)):
                        if (lista_ingresos[i] % 2) == 0:
                            lista_pares.append(lista_ingresos[i])
                            print(f"lista numeros pares ingresados: {lista_pares}")
                else:
                    print("Ingrese numeros para ver esta opcion")
                    break
            case 7:
                posiciones_impares = []
                if bandera_ingreso == True:
                    for i in range (len(lista_ingresos)):
                        if (lista_ingresos[i] % 2) != 0:
                            posiciones_impares.append(i)
                else:
                    print("Ingrese numeros para ver esta opcion")
                    break
            case 8:
                print("Saliendo del programa..")
                break

system("pause")
system("cls")