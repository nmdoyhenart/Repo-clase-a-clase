from validate import validate_num, validate_str

#pedir entero
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None :
    dato = input(f"{mensaje}: ")
    dato = int(dato)

    while validate_num(dato, minimo, maximo) == False:
        print(f"{mensaje_error}\n")
        
        if reintentos == None or reintentos >= 1:
            dato = input(f"{mensaje}: ")
            dato = int(dato)

            if reintentos != None:
                reintentos -= 1
        else:
            dato = None
            break

    return dato

#pedir flotante
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float) -> float|None :
    pedir_numero = input(mensaje)
    pedir_numero = float(pedir_numero)
    validate_num(pedir_numero, minimo, maximo, mensaje_error, reintentos)

    return pedir_numero

#pedir str
def get_str (mensaje: str, mensaje_error: str, longitud: int, reintento)-> str|None:
    palabra_ingresada = input(mensaje)
    palabra_longitud = len(palabra_ingresada)
    validate_str(palabra_longitud, mensaje_error, longitud, reintento)
    return palabra_ingresada
