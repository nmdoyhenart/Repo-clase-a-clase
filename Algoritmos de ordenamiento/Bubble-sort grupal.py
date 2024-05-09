def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Ejemplo de uso:
array = [64, 34, 25, 12, 22, 11, 90]
print("Sin ordenarlo:")
print(array)
bubble_sort(array)
print("Arreglo ordenado:")
print(array)