import tools as t 
import random as r
import math as m  

# Crear una lista al azar sin elementos repetidos, con números de 3 dígitos.  
# Ordenar según  el  dígito  central de  los  números  cargados  en  la lista.
# Utilizar método sort y  el  parámetro  key  para  indicar el  ordenamiento solicitado.

#Funciones
def OrdenarListaDecimalmente(lista):
    lista.sort(key=lambda item: m.floor((item % 100) / 10))

#Programa Principal
def Main():
    cantidadElementos = r.randint(1, 100)

    lista = t.CrearLista(False, cantidadElementos, azarDesde=100, azarHasta=999)

    OrdenarListaDecimalmente(lista)

    print(lista)
Main()