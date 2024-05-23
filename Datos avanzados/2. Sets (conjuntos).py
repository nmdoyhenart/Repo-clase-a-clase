# list = [5,1,5,1,1,1,3,4,9,2,3]
lista = ["Pedro", "Ana", "Ana", "Pedro", "Belen"]       # Ordenamiento, no muestra datos repetidos
set = set(lista)

lista_sin_repetidos = list(set)

print(set)

for nombre in set:      # Recorrer con un for x ej
    print(nombre)

set.add("Juan carlos")        # Compatible con metodos
print(set)

# set.remove("German")    # try, except

set.discard("German")        # "Si no lo encuentra a X, no hace nada"  

elemento = set.pop()       
print(elemento)
elmento = set.pop()         # Borra arbitrariamente el primer elemento
print(elemento)

set.clear()
print(set)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set_a = {"Federico", "Gian", "Aquiles"}
set_b = {"Franco", "Federico", "Agustin"}

set_resultado = set_a.union(set_b)
set_resultado2 = set_a.intersection(set_b)
set_resultado3 = set_b.difference(set_a)

print(set_resultado)
print(set_resultado2)
print(set_resultado3)