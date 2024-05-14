lista = [7, 3, 6]

lista.append(0, 5)             # Primer caracter: la posicion seleccionada, no rompe si no existe la posicion seleccionada
lista.append(2, 9)             # Segundo caracter: lo que ingresa a la lista

print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [7, 3, 6]

lista.insert(0, 4)
lista.insert(10, 10)           # Se rompe pq no existe la posicion 10

print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [7, 3, 6, 9, 3]

for i in range(len(lista)):
    lista.remove(3)
    
for numero in lista:
    if numero == 3:
        lista.remove(numero)

print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [7, 3, 6, 9, 3]

elemento = lista.pop(2)               #M Muestra el elemento en la posición seleccionada
lista_eliminados = []
lista_eliminados.append(elemento)

print(lista)
print(lista_eliminados)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [3, 9, 3]

indice = lista.index(3)       # Encuentra el indice
print(indice)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [3, 9, 3]                # // tambien podrian ser strigs y seran ordenados por orden alfabetico

lista.sort()                       # Ordenamiento expresiones lambda
print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [3, 9, 3] 
lista.reverse()                  # Da vuelta la lista
print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [3, 9, 3] 
lista.clear()                   # Limpia la lista
print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lista = [3, 3, 3, 7, 7, 8]      # // pueden ser strings

cuantos = lista.count(3)
print(cuantos)