cadena = "            hola    "
print(len(cadena))

cadena = cadena.strip()         # Leftstrip , Rightstrip

print(len(cadena))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = "hola mundo"

cadena = cadena.upper()   # / lower

print(cadena)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = "hola mundo"

cadena = cadena.capitalize()

cadena = cadena.replace("la", "@")      # Primer parametro: caracteres buscado, segundo parametro: reemplazo

print(cadena)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = "JS, Python, C, C#"

lenguajes = cadena.split(", ")

for leng in lenguajes:
    print(leng)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

lenguajes = ["Java", "C", "C#", "HTML"]
delimitador = "|"
cadena = delimitador.join(lenguajes)

print(cadena)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = "111"
cadena = cadena.zfill(8)        # Agregar caracteres especificos a la izq

print(cadena)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = "Holamundo"
print(cadena.isalpha())         # Devuelve True / False cuando completa la verificación

cadena = "Holamundo"
print(cadena.isalnum())
                                
cadena = "Holamundo"
print(cadena.isalnum())

cadena = "Holamundo"
print(cadena.isascii())

cadena = "Hola mundo"
print(cadena.isspace())

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

nombre = "german ezequiel"
nombre = nombre.title()

print(nombre)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = "Hola la la la ll la la"
print(cadena.count("l"))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

nombre = "Nicolás"
apellido = "Doyhenart"

print("Su nombre es {0} y su apellido es: {1}".format(nombre,apellido))