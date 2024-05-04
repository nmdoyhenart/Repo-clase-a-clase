from os import system


def sumar_numeros(primer_numero, segundo_numero):
    suma = primer_numero + segundo_numero
    return suma

bandera_seguir = True
while bandera_seguir:
    opcion = int(input("1- Ingresar numeros/n 2-Sumar/n 3-Restar/n 4-Multiplicar/n 5-Dividir/n 6-Salir Elija una opción"))
    
    match opcion:
        case 1: 
            primer_numero = int(input("Ingrese el primer numero: "))
            segundo_numero = int(input("Ingrese otro numero: "))
        case 2:
            if bandera_seguir == True:
                resultado = sumar_numeros(primer_numero, segundo_numero)
                print(f"El resultado de la suma es {resultado}")
            else:
                print("Debe ingresar dos numeros")
        case 3:
            if bandera_seguir == True:
                print("Restando numeros")
            else:
                print("Debe ingresar dos numeros")
        case 4:
            print("Multiplicando numeros")
        case 5:
            print("Dividiendo numeros")
        case 6:
            bandera_seguir = False

system("pause")
system("cls")