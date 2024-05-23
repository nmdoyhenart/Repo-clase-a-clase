diccionario = {
    "nombre": "Tomás",
    "edad": 21,
    "ciudad": "Bs As"
}

print(diccionario["edad"])          # "Clave"
# print(diccionario["ciudad"])

diccionario["dirección"] = "Mitre 750"      # Añadir "Clave"

edad = diccionario.pop("edad")
print(edad)                         # Eliminar "clave"

print(diccionario)

""""""""""""""""""""""""""""""
# Metodo keys
print(diccionario.keys())
""""""""""""""""""""""""""""""
# Metodo items
print(diccionario.items())
""""""""""""""""""""""""""""""
# Metodo values
print(diccionario.values())
""""""""""""""""""""""""""""""

# for clave in diccionario.keys():
    # print(clave)

# for valor in diccionario.values():
    # print(valor)

for clave in diccionario.keys():                    # <-
    print(f"{clave} -> {diccionario[clave]}")       
                                                    # Recorrer diccionario

for clave, valor in diccionario.items():            # <-
    print(f"{clave} -> {valor}")