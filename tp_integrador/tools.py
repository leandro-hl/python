import random as r
import math as m

# Desarrollar  una  función  paracrear  una lista  con  N  elementos al  azar,  
# en  caso  de  no  recibir  N por parámetro, debe crear la lista  con 20 elementos. 
# El rango desde  y hasta también lo debe recibir  por  parámetro  y  en  caso  de  
# omisión  tomar  los  valores  de  1  a100.Si  se  indica  por parámetro debe retornar 
# la lista sin elementos repetidos. 
def CrearLista(elementosRepetidos, cantidadElementos = 20, azarDesde = 1, azarHasta = 100):
    rango = azarHasta - azarDesde + 1

    if(elementosRepetidos and cantidadElementos <= rango):
        return [r.randint(azarDesde, azarHasta) for i in range(cantidadElementos)]

    subRangoUtilizablePorElemento = m.floor(rango / cantidadElementos)
    azarDesdeInicial = azarDesde
    azarHastaInicial = azarDesde + subRangoUtilizablePorElemento
    lista = []

    for i in range(cantidadElementos):
        lista.append(r.randint(azarDesdeInicial, azarHastaInicial))

        if(azarDesdeInicial + subRangoUtilizablePorElemento <= azarHasta):
            azarDesdeInicial += subRangoUtilizablePorElemento
            azarHastaInicial += subRangoUtilizablePorElemento

    return lista

def OrdenarDescendentementeListaNumerica(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux