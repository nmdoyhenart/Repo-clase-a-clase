vector = [5, 7, 9, 1]
largo = len(vector)

for i in range(largo - 1):
    minimo_indice = i

    for j in range(i + 1, largo):
        if vector[j] < vector[minimo_indice]:

            minimo_indice = j
    
    aux = vector[i]
    vector[i] = vector[minimo_indice]
    vector[minimo_indice] = aux

print(vector)