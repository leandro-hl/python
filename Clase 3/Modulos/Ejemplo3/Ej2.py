# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
# según la fecha sea correcta o no. Realizar también un programa para verificar el
# comportamiento de la función

import funciones

EsBisiesto = lambda anio : (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))
'Validar si el año es bisiesto'

def EsFechaValida(dia, mes, anio):
    """
    Determina si una fecha es valida
    
    Devuelve True si la fecha es valida y False si no lo es
    
    Parámetros:
    dia -- numero entero positivo correspondiente al día del mes
    mes -- numero entero positivo correspondiente al mes del año
    anio -- numero entero positivo correspondiente al año calendario
    """
    if (dia < 1) or (mes < 1) or (anio < 1):
        fechaValida = False
    elif (mes > 12):
        fechaValida = False
    elif (mes == 2):
        if (dia <= 28) or (EsBisiesto(anio) and dia == 29):
            fechaValida = True
        else:
            fechaValida = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30):
            fechaValida = True
        else:
            fechaValida = False
    else:
        if (dia <= 31):
            fechaValida = True
        else:
            fechaValida = False
            
    return fechaValida


#Programa Principal
print("Ejercicio 1.2: Validar una fecha")
dia = funciones.IngresarPositivo("Ingrese día: ")
mes = funciones.IngresarPositivo("Ingrese mes: ")
año = funciones.IngresarPositivo("Ingrese año: ")

if (EsFechaValida(dia, mes, año)):
    print("La fecha ingresada es válida")
else:
    print("La fecha ingresada no es válida")