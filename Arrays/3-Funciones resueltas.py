def mostrar_lista(lista: list, ilogico: int) -> bool:
    """
    Muestra lista

    Args:
        lista (list): lista que se va a mostrar
        ilogico (int): valor del elemento vacio

    Returns:
        bool: False si no se pudo mostrar | True si se pudo mostrar
    """
    exito = False
    if type(lista) == list and type(ilogico) == int:
        exito = True
        for i in range(len(lista)):
            if lista[i] != ilogico:
                print(f"{i + 1} -> {lista[i]}")    

    return exito

def preguntar_continua(mensaje: str) -> bool:
    bandera_seguir = True
    seguir = input(mensaje)
    if seguir != "si":
        bandera_seguir = False

    return bandera_seguir

def cargar_valor(lista, posicion, ilogico) -> bool:
    exito = False
    if lista[posicion] == ilogico:
        numero = get_int("Ingrese un numero: ", 1000, 1)
        lista[posicion] = numero
        exito = True
    
    return exito

def get_int(mensaje, maximo, min):
    pass
###############################################

mi_lista = [-1] * 5

bandera_seguir = True

while bandera_seguir == True:
    posicion = get_int("Ingrese posicion", len(mi_lista), 1)

    if not cargar_valor(mi_lista, posicion - 1, -1):
        print("La posicion ya contiene un valor")
    
    bandera_seguir = preguntar_continua("Quiere ingresar otro? si/no: ")

if not mostrar_lista(mi_lista, -1):
    print("Hubo un error al intentar mostrar la lista")

otra_lista = [5,9,7,8,5,7,1]

if not mostrar_lista(otra_lista, 7):
    print("lalal")
