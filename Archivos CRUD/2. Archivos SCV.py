# C S V

# nombre = ["Maria","Hernán","Carlos"]
# apellidos = ["Ruiz","Fernandez","Lopez"]
# edades = [23,35,67]

# with open("agenda.csv", "w") as archivo:
#     for i in range(len(nombre)):
#         registro = f"{nombre[i]},{apellidos[i]},{edades[i]}\n"
#         archivo.write(registro)
        
with open("agenda.csv", "r") as archivo:
    for linea in archivo:
        registro = linea.split(",")
        print(f"{registro[0]} == {registro[1]} == {registro[2]}")