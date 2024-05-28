"""
Apertura de Archivos
Para trabajar con archivos en Python, primero se necesita abrir el archivo.
Esto se hace usando la función open(), que devuelve un objeto de archivo.
La función open() toma dos argumentos principales: el nombre del archivo y el modo en que
deseas abrirlo.

Modos de Apertura:

'r': Modo de lectura (read). Abre un archivo para lectura (predeterminado). Si el archivo no
existe, genera un error.

'w': Modo de escritura (write). Abre un archivo para escritura. Si el archivo no existe, lo
crea. Si el archivo existe, trunca su contenido (lo borra).

'a': Modo de anexado (append). Abre un archivo para añadir contenido. Si el archivo no
existe, lo crea.
El nuevo contenido se añade al final del archivo.

'r+': Modo de lectura y escritura. Abre un archivo para lectura y escritura. El archivo debe
existir.

'w+': Modo de lectura y escritura. Abre un archivo para lectura y escritura. Si el archivo
no existe, lo crea.
Si el archivo existe, trunca su contenido.

'a+': Modo de lectura y anexado. Abre un archivo para lectura y anexado. Si el archivo no
existe, lo crea.
El nuevo contenido se añade al final del archivo.
"""

# Leemos el archivo dentro del directorio asignando la ruta
archivo = open(r'Apuntes\Archivos txt\ejemplo.txt', 'r')
cadena_archivo_con_ruta = archivo.read()
print(cadena_archivo_con_ruta)


# Creamos el archivo en modo escritura
archivo = open('ejemplo.txt', 'w')


# open sin definir el modo lo abre sin hacer nada, si no existe tira excepcion al tratar de crear

# archivo_sin_extension = open('ejemplo')
# Escribir en un archivo:
# forma simple, \n porque write por defecto añade la linea al final:
archivo.write("Hola gente magenta\n")
archivo.write("Hola, mundo!\n")

# forma 2:
# with hace que el archivo se cierra automaticamente despues de que se termina la operacion
with open('ejemplo.txt', 'w') as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Esta es una segunda línea.\n")
    
# Formaas de leer archivos:

# abrimos el archivo porque el with de arriba lo cerró:
archivo = open('ejemplo.txt', 'r')

# Leer todo el contenido de una vez:
contenido = archivo.read()
print(contenido)

# Leer linea por linea
for linea in archivo:
    print(linea)

# Leer una sola linea
linea = archivo.readline()
print(linea)
 
# Leer todas las lineas y almacenarlas en una lista
lineas = archivo.readlines()
print(lineas)

# Leer todo el contenido del archivo con with
with open('ejemplo.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Leer el archivo línea por línea con with
with open('ejemplo.txt', 'r') as archivo:
    print("Leyendo línea por línea:")
for linea in archivo:
    print(linea, end='')

# Leer todas las líneas y almacenarlas en una lista con with
with open('ejemplo.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print("\nContenido almacenado en una lista:")
    print(lineas)

# Añadir una línea al archivo existente
with open('ejemplo.txt', 'a') as archivo:
    archivo.write("Añadiendo una nueva línea al final.\n")

# Escribir una lista
lista = ["Margaret", "Terry", "Toby"]
with open('lista_nombres.txt', 'a') as archivo:
    for nombre in lista:
        archivo.write(f"{nombre}\n")

# Leer lista
with open('lista_nombres.txt', 'r') as archivo:
    for nombre in archivo:
        print(nombre)

# Cerramos el archivo
archivo.close()

# Retorna si se cerro el archivo
print(archivo.closed)

# Retorna el nombre del archivo
print(archivo.name)

# Retorna el modo de apertura
print(archivo.mode)

# Retorna si es de escritura
print(archivo.writable())

# Retorna si es de lectura, tiene que estar abierto sino tira excepcion
print(archivo.readable())