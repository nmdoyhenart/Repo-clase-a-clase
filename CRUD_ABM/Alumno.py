# Create

def crear_alumno(dni: int, nombre: str, apellido: str, nota: int) -> dict:
    diccionario_alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "nota": nota
    }

    return diccionario_alumno

# Hay limitaciones?
def ingresar_alumno_lista(lista_alumnos: list) -> None:
    dni = int(input("Ingrese su DNI: ")) # get_int: verificar valor numerico, rango
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nota = int(input("Ingrese su nota: "))

    diccionario_alumno = crear_alumno(dni, nombre, apellido, nota)

    lista_alumnos.append(diccionario_alumno)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Muestro de datos / Read

def mostrar_alumno(un_alumno: dict):
    print(f"{un_alumno["dni"]:10}{un_alumno["nombre"]:>12}{un_alumno["apellido"]:>12}{un_alumno["nota"]:>4}")

def mostrar_todos(lista_alumnos: list[dict]):
    for alumno in lista_alumnos:
        mostrar_alumno(alumno)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Update

def modificar_alumno(lista_alumnos: list[dict], dni: int):        # Retorne: si encontro el dato y si pudo modificar
    for alumno in lista_alumnos:                                  # Dar opción de modificar el dato
        if alumno["dni"] == dni:                                  # Crear copia, modificar esta y luego dejarla con el cambio si esta bn
            print("Alumno encontrado")
            nueva_nota = int(input("Ingrese la nueva nota: "))
            alumno["nota"] = nueva_nota
            break

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Delete

def eleminar_alumno(lista_alumnos: list[dict], dni: int):
    alumno_eliminado = None
    for alumno in lista_alumnos:                                  
        if alumno["dni"] == dni:                                  
            print("Alumno encontrado nashe")
            alumno_eliminado = alumno
            break

    if alumno_eliminado != None:
        lista_alumnos.remove(alumno_eliminado)

    return alumno_eliminado