"""
Nombre: Nicolás
Apellido: Doyhenart

Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:

-Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
-Mostrar la recaudación de todos los coches y líneas.
-Calcular y mostrar recaudación por línea.
-Calcular y mostrar recaudación por coche.
-Calcular y mostrar la recaudación total.
-Salir

Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
"""
from os import system
import random

legajo = random.randint(1000,2000)

lineas = [[160, 74, 79],
          [1,2,3,4,5]]

recaudacion_matriz = []

# def generar_legajos(filas, columnas):
#     inicio = 1000
#     legajos = []
#     for i in range(filas):
#         nueva_fila = []
#         for j in range(columnas):
#             nueva_fila += [inicio]
#             inicio += 1
#         legajos += [nueva_fila]
#     return legajos


# legajos = generar_legajos(3, 5)
# for fila in legajos:
#     print(fila)


bandera_ingreso = True
while bandera_ingreso:
    opcion = int(input("""1-Cargar planilla.\n2-Mostrar la recaudación de todos los coches y lineas.\n3-Calcular y mostrar la recaudación por coche\n4-Calcular y mostrar la recaudación total.\n5-Salir\nElija una opcion: """))

    match opcion:
            case 1:
                while True:
                    linea = int(input("Ingrese la línea de colectivo que maneja: "))
                    if linea == 160 or linea == 74 or linea == 79:
                        break
                    else:
                        print("ERROR, línea inválida")
                
                while True:
                    coche = int(input("Ingrese el coche que maneja: "))
                    if coche == 1 or coche == 2 or coche == 3 or coche == 4 or coche == 5:
                        break
                    else:
                        print("ERROR, coche invalido")
                
                print(f"Este es su numero de legajo: {legajo}")

                while True:
                    recaudacion = float(int(input("Ingrese la recaudacion del dia: ")))
                    if recaudacion > 1:
                        break
                    else:
                        print("ERROR, reingrese un valor valido.")
                    
                    recaudacion = recaudacion_matriz
                
            case 2:
                print("Recaudación de coches y lineas")
            case 3:
                print("Recaudación por coche")
            case 4:
                print("Recaudación total")
            case 5:
                print("Saliendo del programa..")
                break

system("pause")
system("cls")