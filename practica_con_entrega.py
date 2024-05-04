"""
Nombre: Nicolás
Apellido: Doyhenart

Fecha: 23/04

Desarrollar una función que reciba como parametros el precio de un producto y el porcentaje de descuento que se aplicara. La funcion retornara el precio del producto con descuento.
"""
def producto_venta(precio: int, porcentaje_descuento: int)-> int|None:
    descuento = precio * (porcentaje_descuento / 100)
    resultado = precio - descuento
    return resultado

precio = 300
porcentaje_descuento = 50
resultado = producto_venta(precio, porcentaje_descuento)
print(resultado)