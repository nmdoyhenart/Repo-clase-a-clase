# for i in range(10, -1, -1):
#     print(i)

###################################

# i = 10
# while i>=0:
#     print(i)
#     i -= 1

####################################
    
# def cuenta_regresiva(numero: int):
#     if numero != -1:
#         print(numero)
#         cuenta_regresiva(numero - 1)  #RECURSVIDAD 

# cuenta_regresiva(10)
# cuenta_regresiva(997)

# numero = 5
# resultado = 1

####################################

# for i in range(numero, 0, -1):         #PRIMER CASO FACTORIAL
#     resultado *= i
    
# print(resultado)

####################################

def calcular_factorial(numero: int):
    if numero == 0:
        factorial = 1
    else:
        factorial = numero * calcular_factorial(numero - 1)
    return factorial

f = calcular_factorial(5)
print(f)

