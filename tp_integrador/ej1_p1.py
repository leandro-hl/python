import tools as t 
import random as r
import math as m  

# Crear  una  lista  con  N  elementos  al  azar entre  1  y  100.
# Mostrar  el promedio  y  aquellos  elementos  que  sean  mayores al  promedio, 
# ordenados de menor a mayor(Utilizar la funciónsum).a.Crear la nueva lista utilizando 
# el métodopor comprensión.b.Crear la nueva lista utilizando la funciónfilter.

#Funciones
def CalcularPromedio(lista):
    total = sum(lista)
    return total / len(lista)

def ObtenerItemsMayoresAlPromedio(promedio, lista):
    return [i for i in filter(lambda item: item > promedio, lista)]

#Programa Principal
def Main():
    cantidadElementos = r.randint(1, 100)

    lista = t.CrearLista(True, cantidadElementos)

    promedio = CalcularPromedio(lista)

    numerosMayoresAlPromedio = ObtenerItemsMayoresAlPromedio(promedio, lista)

    t.OrdenarDescendentementeListaNumerica(numerosMayoresAlPromedio)
    
    print(promedio)
    print(numerosMayoresAlPromedio)

Main()