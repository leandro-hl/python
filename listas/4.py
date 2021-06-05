# Definir una función superposición() que reciba como parámetros dos listas de cualquier
# tipo y devuelva True si tienen al menos un elemento en común, o False en
# caso contrario. Desarrollar un programa para verificar su comportamiento.

def superposicion(lista1, lista2):
    elemtoEnComun = False

    for i, valor in enumerate(lista1):
        if not elemtoEnComun and valor in lista2:
            elemtoEnComun = True

    return elemtoEnComun