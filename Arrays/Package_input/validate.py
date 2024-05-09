from .input import get_string, get_int, get_float
"""
VALIDATE LENGHT
"""

def validate_lenght(mensaje: str, mensaje_error: str, longitud: int, reintentos: int)-> str|None:
    palabra_longitud = len(mensaje)
    contador_reintentos = 0
    
    while palabra_longitud != longitud:
        contador_reintentos += 1
        
        if contador_reintentos < reintentos:
            mensaje = input(mensaje_error)
            palabra_longitud = len(mensaje)
            
        else:
            mensaje = None
            break
    
    return mensaje

"""
VALIDATE NUMBER
"""

def validate_number(mensaje: str, mensaje_error: str, minimo: int|float, maximo: int|float, reintentos: int) -> int|float|None:
    numero = int(mensaje)
    numero = float(mensaje)
    contador_reintentos = 0
    
    while numero != minimo or numero != maximo:
        contador_reintentos += 1

        if contador_reintentos < reintentos:
            mensaje = input(mensaje_error)
        
        else:
            mensaje = None
            break
    
    return numero
    