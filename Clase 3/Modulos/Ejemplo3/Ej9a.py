# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
# expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
#   a. Sumar N días a una fecha.
#   b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

import funciones
import Ej2b as Ej2

def DiaSiguiente(dia, mes, anio):
    """
    Determina el dia siguiente a una fecha ingresada
    
    Devuelve el dia, mes y año correspondientes al dia siguiente de la fecha ingresada
    
    Parámetros:
    dia -- numero entero positivo correspondiente al día del mes
    mes -- numero entero positivo correspondiente al mes del año
    anio -- numero entero positivo correspondiente al año calendario
    """
    if (Ej2.EsFechaValida(dia + 1, mes, anio)):
        dia = dia + 1
    elif (Ej2.EsFechaValida(1, mes + 1, anio)):
        dia = 1
        mes = mes + 1
    else:
        dia = 1
        mes = 1
        anio = anio + 1
    
    return dia, mes, anio

#Programa Principal
print("Ejercicio 1.9 a: Sumar dias a una fecha")
print("Ingrese una fecha")
dia = funciones.IngresarPositivo("Ingrese el día: ")
mes = funciones.IngresarPositivo("Ingrese el mes: ")
anio = funciones.IngresarPositivo("Ingrese el año: ")
if (Ej2.EsFechaValida(dia, mes, anio)):
    dias = funciones.IngresarPositivo("Días a sumar: ")
    for i in range(dias):
        dia, mes, anio = DiaSiguiente(dia, mes, anio)
    print("La nueva fecha es:", end=" ")
    print(dia, mes, anio, sep="/")
else:
    print("La fecha ingresada no es valida")
    