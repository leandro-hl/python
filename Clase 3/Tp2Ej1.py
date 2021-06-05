#1. Desarrollar cada una de las siguientes funciones y escribir un
#   programa que permita verificar su funcionamiento imprimiendo la
#   lista luego de invocar a cada función:
#   a. Cargar una lista con números al azar de cuatro dígitos. La
#      cantidad de elementos también será un número al azar de dos dígitos.
#   b. Calcular y devolver la sumatoria de todos los elementos de la lista
#      anterior.
#   c. Eliminar todas las apariciones de un valor en la lista anterior. El
#      valor a eliminar se ingresa desde el teclado y la función lo recibe
#      como parámetro.
#   d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar
#      listas auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

import random

def GenerarListaAleatoria():
    lista = []
    for x in range(random.randint(10,99)):
        lista.append(random.randint(1000,9999))
    
    return lista

def SumaLista(lista):
    suma = 0
    for x in lista:
        suma += x
    
    return suma

def RemoverElemento(lista, n):
    for x in range(-1,-len(lista)-1,-1):
        if lista[x] == n: lista.pop(x)
        
def EsCapicua(lista):
    i = 0
    while i < len(lista)//2 and lista[i] == lista[len(lista)-i-1]:
        i += 1
    
    return i >= len(lista)//2
    
    