# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
# expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
#   a. Sumar N días a una fecha.
#   b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

import funciones
import Ej2b
import Ej9ab

EsMenorFecha = lambda dia1, mes1, anio1, dia2, mes2, anio2 : (anio1 < anio2 or (anio1 == anio2 and mes1 < mes2) or (anio1 == anio2 and mes1 == mes2 and dia1 < dia2))
'Validar si una fecha es anterior (menor) a otra'


def main():
    #Diferencia entre fechas
    print("Ejercicio 1.9 b: Diferencia entre dos fechas")
    print("Ingrese una fecha")
    dia1 = funciones.IngresarPositivo("Ingrese el día: ")
    mes1 = funciones.IngresarPositivo("Ingrese el mes: ")
    anio1 = funciones.IngresarPositivo("Ingrese el año: ")
    print("Ingrese otra fecha")
    dia2 = funciones.IngresarPositivo("Ingrese el día: ")
    mes2 = funciones.IngresarPositivo("Ingrese el mes: ")
    anio2 = funciones.IngresarPositivo("Ingrese el año: ")

    if (funciones.EsFechaValida(dia1, mes1, anio1) and funciones.EsFechaValida(dia2, mes2, anio2)):
        diferencia = 0
        if (funciones.EsMenorFecha(dia1, mes1, anio1, dia2, mes2, anio2)):
            while (funciones.EsMenorFecha(dia1, mes1, anio1, dia2, mes2, anio2)):
                diferencia = diferencia + 1
                dia1, mes1, anio1 = funciones.DiaSiguiente(dia1, mes1, anio1)
        else:
            while (funciones.EsMenorFecha(dia2, mes2, anio2, dia1, mes1, anio1)):
                diferencia = diferencia + 1
                dia2, mes2, anio2 = funciones.DiaSiguiente(dia2, mes2, anio2)
        print("Hay",diferencia,"días de diferencia entre las fechas ingresadas")
    else:
        print("Al menos una de las fechas ingresadas no es valida")

if __name__ == "__main__":
    main()