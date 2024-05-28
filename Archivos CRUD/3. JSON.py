import json

data = {}
data["Personas"] = []

data["Personas"].append({"Nombre": "Juan", "Edad": 32})
data["Personas"].append({"Nombre": "Carlos", "Edad": 72})
data["Personas"].append({"Nombre": "Aquiles", "Edad": 18})              # Creación
data["Personas"].append({"Nombre": "Joan", "Edad": 18})

data["Producto"] = "Sprite 2.75lts"

with open("personas.json", "w") as archivo:
    json.dump(data, archivo, indent = 4)

""""""""""""""""""""""""""""""""""""""""""""""""

with open("personas.json", "r") as archivo:       # Mostrar el json
    diccionario = json.load(archivo)

""""""""""""""""""""""""""""""""""""""""""""""""

personas = diccionario["Personas"]                  
producto = diccionario["Producto"]
for personas in personas:
    print(f"{personas["Nombre"]} -- {personas["Edad"]}")            # Muestro con desglose
    
print(producto)

""""""""""""""""""""""""""""""""""""""""""""""""

