"""
FLOAT
"""
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float) -> float|None:
    pedir_numero = input(mensaje)
    pedir_numero = float(pedir_numero)
    contador_intentos = 0
    while pedir_numero < minimo or pedir_numero > maximo:
        pedir_numero = input(mensaje_error)
        pedir_numero = float(pedir_numero)
        contador_intentos += 1
        if contador_intentos == reintentos:
            return None
            break
    return pedir_numero

resultado = get_float("ingrese un numero flotante: ", "ERROR, reingrese un numero flotante: ):", 0.1,100000,1,  2)
print(resultado)

"""
INT
"""

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    numero = input(mensaje)
    numero = int(numero)
    contador_intentos = 0
    while numero < minimo or numero > maximo:
        numero = input(f"ERROR, {mensaje_error}")
        numero = int(numero)
        contador_intentos += 1
        if contador_intentos == reintentos:
            return None
            break
    return numero       

resultado = get_int("Ingrese un numero entero ","REingrese un numero: ", 0, 1000000, 3) #// entre 25 y 90
print(resultado)

"""
STRING
"""

def get_string(mensaje: str, mensaje_error: str, longitud: int, reintento)-> str|None:
    palabra_ingresada = input(mensaje)
    palabra_longitud = len(palabra_ingresada)
    contador = 0
    while palabra_longitud > longitud:
        palabra_ingresada = input(mensaje_error)
        palabra_longitud = len(palabra_ingresada)
        contador += 1
        if contador == reintento:
            return None
            break
    return palabra_ingresada

resultado = get_string("Ingrese una cadena: ", "ERROR, reingrese una cadena: ", 10, 2)
print(resultado)