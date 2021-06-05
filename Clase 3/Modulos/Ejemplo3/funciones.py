"""Funciones genericas para la resolucion de ejercicios"""
from random import randint

def IngresarPositivo(texto):
    'Solicita el ingreso de un numero entero positivo'
    numero = int(input(texto))
    while numero < 1:
        print("El numero ingresado no es valido.")
        numero = int(input(texto))
    
    return numero

def GenerarListaRandom(tamaño = 10, minimo = 0, maximo = 100):
    """
    Genera una lista de valores aleatorios
    
    Devuelve una nueva lista con valores aleatorios
    
    Parámetros:
    tamaño -- numero entero. Cantidad de elementos a generar (10)
    minimo -- numero entero. Minimo valor a agregar en la lista (0)
    maximo -- numero entero. Maximo valor a agregar en la lista (100)
    """
    lista = []
    for i in range(tamaño):
        lista.append(randint(minimo, maximo))
    
    return lista