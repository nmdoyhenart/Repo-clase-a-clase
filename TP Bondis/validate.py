def validate_num (numero:int|float, minimo:int|float, maximo:int|float) -> bool|None: 
    validacion =  True

    if minimo != None:
        validacion = numero >= minimo
    if maximo != None:
        validacion = numero <= maximo
        
    return validacion
    
def validate_str (palabra_longitud: int, mensaje_error: str, longitud: int, reintento: int):
    contador = 0
    if palabra_longitud > longitud:
        while palabra_longitud > longitud:
            palabra_ingresada = input(mensaje_error)
            palabra_longitud = len(palabra_ingresada)
            contador += 1
            if contador == reintento:
                palabra_ingresada = None
                break
    else:
        pass
    return palabra_ingresada