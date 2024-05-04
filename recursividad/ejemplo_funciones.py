MENSAJE_INICIAL = "Hola a todos!!"

##########################CASO 1###############################

def sumar_numeros_1():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"La suma es {suma}.")

##########################CASO 2###############################

def sumar_numeros_2(un_numero, otro_numero):
    suma = un_numero + otro_numero

    print(f"La suma es {suma}.")

##########################CASO 3###############################

def sumar_numeros_3():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)                                 

    suma = un_numero + otro_numero

    return suma

##########################CASO 4################################

def sumar_numeros_4(un_numero, otro_numero):
    suma = un_numero + otro_numero

    return suma

################################################################

def presentar_persona(nombre: str, edad: int, mail = None):
    if mail == None: #if not mail:
        print(f"Hola me llamo {nombre} y tengo {edad} años.")
    else:
        print(f"Hola me llamo {nombre} y tengo {edad} años, mi Mail es: {mail}.")

nombre_persona = "Nicolás"
edad_persona = 18

presentar_persona("Giovanni", 25)
presentar_persona("Germán", 35, "germancito123@gmail.com")
presentar_persona(edad = edad_persona, nombre = nombre_persona, mail = "nidoyhe@gmail.com")