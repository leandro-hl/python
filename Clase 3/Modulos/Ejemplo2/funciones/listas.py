'Funciones relacionadas al manejo de listas'
from random import randint

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
