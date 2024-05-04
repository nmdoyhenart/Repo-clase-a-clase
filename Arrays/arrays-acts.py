"""
Nombre: Nicolás
Apellido: Doyhenart

Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe 
reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente 
reemplazo y luego retornar la cantidad total de reemplazos realizados.
"""
import Package_input

def reemplazar_nombres (lista: list, nombre_reemplazo: str, nombre: str ):
    contador_reemplazados = 0
    for i in range(len(lista)):
        if lista[i] == nombre_reemplazo:
            lista[i] = nombre
            contador_reemplazados += 1
    print(lista)
    return contador_reemplazados

lista_nom = ["juan", "jose", "octa", "juan", "santi", "juan"]
nombre_a_reemplazar = #get_string("ingrese el nombre que quiera reemplazar: ", "ingrese un NOMBRE que quiera reemplazar: ", 100, 2)
nombre_a_poner = #get_string("ingrese un numbro: ", "ingrese un NOMBRE que quiera poner: ", 100, 2)

reemplazo = reemplazar_nombres(lista_nom, nombre_a_reemplazar, nombre_a_poner)
print(reemplazo)

