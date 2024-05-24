# Testing

# lista_alumnos = [
#     {'dni': 3, 'nombre': 'Agatha', 'apellido': 'Kerva', 'nota': 8}, 
#     {'dni': 8, 'nombre': 'Dibu', 'apellido': 'Martínez', 'nota': 10},
#     {'dni': 11, 'nombre': 'Nicolás', 'apellido': 'Zelarayan', 'nota': 4},
#     {'dni': 13, 'nombre': 'Leandro', 'apellido': 'Paredes', 'nota': 2},
#     {'dni': 19, 'nombre': 'Leandro', 'apellido': 'Díaz', 'nota': 1},
#     {'dni': 1, 'nombre': 'Sebastían', 'apellido': 'Domínguez', 'nota': 4}
# ]

# # mostrar_un_alumno(lista_alumnos[1])
# mostrar_todos(lista_alumnos)

# ######################################################

# modificar_alumno(lista_alumnos, 11)
# mostrar_todos(lista_alumnos)

# ######################################################

# eliminado = eleminar_alumno(lista_alumnos, 2)
# print("ELIMINADO")
# mostrar_alumno(eliminado)
# mostrar_todos(lista_alumnos)

# # ingresar_alumno_lista(lista_alumnos)
# # ingresar_alumno_lista(lista_alumnos)

# # print(lista_alumnos)

from Alumno import *
from os import system

def elegir_opcion():
    opcion = input("""MENU\n1. Ingresar\n2. Modificar\n3. Eliminar\n4. Mostrar todos\n5. Salir\nElija una opción:
""")
    return opcion

lista_alumnos = [
    {'dni': 3, 'nombre': 'Agatha', 'apellido': 'Kerva', 'nota': 8}, 
    {'dni': 8, 'nombre': 'Dibu', 'apellido': 'Martínez', 'nota': 10},
    {'dni': 11, 'nombre': 'Nicolás', 'apellido': 'Zelarayan', 'nota': 4},
    {'dni': 13, 'nombre': 'Leandro', 'apellido': 'Paredes', 'nota': 2},
    {'dni': 19, 'nombre': 'Leandro', 'apellido': 'Díaz', 'nota': 1},
    {'dni': 1, 'nombre': 'Sebastían', 'apellido': 'Domínguez', 'nota': 4}
]

system("cls")

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            ingresar_alumno_lista(lista_alumnos)
        case "2":
            dni = int(input("Ingrese el DNI a modificar: "))
            modificar_alumno(lista_alumnos, dni)
        case "3":
            dni = int(input("Ingrese el DNI a eliminar: "))
            eleminar_alumno(lista_alumnos, dni)
        case "4":
            system("cls")
            mostrar_todos(lista_alumnos)
        case "5":
            break
    
    system("pause")
    system("cls")