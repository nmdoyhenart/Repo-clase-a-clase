from Data import *

# def generar_csv(path: str, lista: list):
#     with open(path, "w", encoding = "utf8") as archivo:
#         for tema in lista:
#             cadena = f"{tema['title']},{tema['views']},{tema['url']}\n"        # Creación
#             archivo.write(cadena)


# generar_csv("playlistBZRP.csv", lista_bzrp)

""""""""""""""""""""""""""""""""""""""""""""""""""
import re

def parse_csv(path: str)-> list:
    lista = []
    
    with open(path, "r", encoding = "utf8") as archivo:
        for linea in archivo:
            diccionario = {}
            valores = re.split(",|\n", linea)
            diccionario["title"] = valores[0]
            diccionario["views"] = valores[1]
            diccionario["url"] = valores[2]
            lista.append(diccionario)
    
    return lista

lista = parse_csv("playlistBZRP.csv")
print(lista)

""""""""""""""""""""""""""""""""""""""""""""""""""
import json

# def generar_json(path: str, lista: list):
#     with open(path, "w", encoding = "utf8") as archivo:
#         json.dump(lista, archivo, indent = 4)
        
# play = {}
# play["Lista"] = lista_bzrp

# generar_json("lista.json", play)

""""""""""""""""""""""""""""""""""""""""""""""""""

def parsear_json(path: str)-> list:
    with open(path, "r", encoding = "utf8") as archivo:
        diccionario = json.load(archivo)
        
    return diccionario["Lista"]

lista = parsear_json("lista.json")
print(lista)