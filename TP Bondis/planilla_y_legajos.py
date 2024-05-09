import random
from input import get_int

def generar_legajos(cantidad:int) -> list:
    lista_legajos = [0] * cantidad

    for i in range(len(lista_legajos)):
        nuevo_legajo = random.randint(1000, 9999)
        lista_legajos[i] = nuevo_legajo

    return lista_legajos

def validar_legajo(legajo:int, lista_legajos: list) -> bool:
    validacion = False

    for i in range(len(lista_legajos)):
        if lista_legajos[i] == legajo:
            validacion = True
            break

    return validacion

def cargar_planilla(legajos : list, colectivos : list):
    legajo = get_int("Legajo", "Invalido", 1000, 9999, 5)

    if validar_legajo(legajo, legajos):
        linea = get_int("Linea", "Invalido", 160, 74, 79)
        coche = get_int("Coche", "Invalido", 1, 2, 3, 4, 5)

        recaudacion = get_int("Recaudacion", "Invalido", 0, 10 ** 100, 5)
        colectivos[linea - 1][coche - 1] += recaudacion
        print("Planilla Cargada.")
    else:
        print("Legajo no registrado.")