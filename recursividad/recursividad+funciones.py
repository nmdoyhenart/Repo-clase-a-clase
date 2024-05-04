"""
Nombre: Nicolás
Apellido: Doyhenart

Realizar una función recursiva que calcule la suma de los primeros números naturales:
"""
# def sumar_naturales(numero: int)-> int:
#     if numero == 0:
#         suma = 0
#     else:
#         suma = numero + sumar_naturales(numero - 1)
#     return suma

# numero_suma = 10

# resultado = sumar_naturales(numero_suma)
# print(resultado)

"""
Realizar una función recursiva que calcule la potencia de un número:
"""
# def calcular_potencia(base: int, exponente: int)-> int:
#     if exponente < 0:
#        return 1
#     else:
#         return base * calcular_potencia(base, exponente - 1)

# base = 2
# exponente = 6

# resultado = calcular_potencia(base, exponente)
# print(resultado)

"""
Realizar una función recursiva que la suma de los dígitos de un número:
"""
# def sumar_digitos(numero: int)-> int:
#     if numero < 10:
#         return numero
#     else:
#         return numero % 10 + sumar_digitos(numero // 10)
    
# digito = 363
# resultado = sumar_digitos(digito)
# print(resultado)

"""
Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo
"""

from Package_input import input

def calcular_fibonacci(numero: int)-> int:
    if numero < 2:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

for iteracion in range(2):
    print(calcular_fibonacci(iteracion))

def get_int(mensaje: str, mensaje_error: str, maximo: int, minimo: int, reintentos: int):
    while numero < minimo or numero > maximo:
        numero = input(f"ERROR, {mensaje_error}")
        numero = int(numero)
        contador_intentos += 1
        if contador_intentos == reintentos:
            return None
            break
    return numero       


    
