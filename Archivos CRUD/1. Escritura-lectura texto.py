# archivo = open("texto.txt", "w+")
# archivo.write("Los pibes estan re manija")
# cadena = archivo.read()
# archivo.close()
# print(cadena)

lista = ["Nicolás","Agustín","Ezequiel"]
with open("lista_nombres.txt", "r") as archivo:
    for nombre in lista:
        archivo.write(f"{nombre}\n")
        
with open("lista_nombres") as archivo:
    lista = archivo.readlines()

for nombre in lista:
    print(nombre, end = "")
    
lista = []
with open("lista_nombres") as archivo:
    for linea in archivo:
        lista.append(linea)
        
print(lista)