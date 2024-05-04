from os import system

def ingreso_num(minimo, maximo):
    numero = int(input("ingrese el numero que desee:"))
   
        numero = int(input("su numero ingresado esta fuera de parametro; ingrese otro numero:"))
    return numero
lista_ingresada = []
bandera_ingreso = False
contador_positivos = 0
contador_negativos = 0
while True:
    opciones = input(
    """Sus opciones son:
    A_ ingresar los 10 numeros. 
    B_ Mostrar la cantidad de números positivos y negativos. 
    C_ Mostrar la sumatoria de los números pares. 
    D_Informar el mayor de los números impares. 
    E_Listar todos los números ingresados. 
    F_Listar todos los números pares. 
    G_ Listar los números de las posiciones impares. 
    H_ Salir
    Ingrese una letra segun lo que desee:""")
    match opciones:
        case "A":
            bandera_ingreso = True
            for ingreso in range(5):
                numeros_ingresados = ingreso_num(-1000, 1000)
                lista_ingresada.append(numeros_ingresados)
        case "B":
            if bandera_ingreso == True:
                for i in range(len(lista_ingresada)):
                    if lista_ingresada[i] > 0:
                        contador_positivos += 1
                    else:
                        contador_negativos += 1
                print(f"El total de numeros positivos fue de {contador_positivos}, y los numeros negativos fueron {contador_negativos}.")
            else : 
                print("No ingreso ningun valor, debe ingresar sus numeros:")
        case "C":
            suma_numeros_pares = 0
            if bandera_ingreso == True:
                for i in range (len(lista_ingresada)):
                    if (lista_ingresada[i] % 2) == 0:
                        suma_numeros_pares += lista_ingresada[i]
                print(f"La sumatoria de todos los numeros ingresados pares es {suma_numeros_pares}.")
            else : 
                print("No ingreso ningun valor, debe ingresar sus numeros:")
        case "D":
            mayor_impares = 0
            if bandera_ingreso == True:
                for i in range (len(lista_ingresada)):
                    if (lista_ingresada[i] % 2) != 0 and lista_ingresada[i] > mayor_impares:
                        mayor_impares = lista_ingresada[i]
                print(f"el mayor de los numeros impares ingresados es {mayor_impares}")
            else : 
                print("No ingreso ningun valor, debe ingresar sus numeros:")
        case "E":
            if bandera_ingreso == True:
                print(f" Los numeros que usted ingreso enlistados: {lista_ingresada}")
            else : 
                print("No ingreso ningun valor, debe ingresar sus numeros:")
        case "F":
            lista_pares = []
            if bandera_ingreso == True:
                for i in range (len(lista_ingresada)):
                    if (lista_ingresada[i] % 2) == 0:
                        lista_pares.append(lista_ingresada[i])
                print(f"lista numeros pares ingresados: {lista_pares}")
            else : 
                print("No ingreso ningun valor, debe ingresar sus numeros:")
        case "G":
            posiciones_impares = []
            if bandera_ingreso == True:
                for i in range (len(lista_ingresada)):
                    if (lista_ingresada[i] % 2) != 0:
                        posiciones_impares.append(i)
                print(f"las posiciones de los numeros impares son: {posiciones_impares}")
            else : 
                print("No ingreso ningun valor, debe ingresar sus numeros:")
        case "H":
            break

    system("pause")
    system("cls")




