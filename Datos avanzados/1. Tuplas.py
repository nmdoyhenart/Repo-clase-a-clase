tupla = (4,6,9)   

print(tupla[0])
for elemento in tupla:
    print(elemento)

# tupla[0] = 25   Execepción
    
a, b, c = tupla

print(a)
print(b)            # Desglosar tuplas
print(c)

"""""""""""""""""""""""EJ"""""""""""""""""""""""""""""""""

def hacer(punto):
    x = punto[0]
    y = punto[1]
    # x, y = punto

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

tupla = (5,4,6,4)

print(tupla.count(4))
print(tupla.index(40))