# Desarrollar una función para crear una lista con N elementos al azar,
# en caso de no recibir N por parámetro, debe crear la lista con 20
# elementos. El rango desde y hasta también lo debe recibir por
# parámetro y en caso de omisión tomar los valores de 1 a 100.
# Si se indica por parámetro debe retornar la lista sin elementos
# repetidos.

from random import randint as rndm

def generarLista(cantElem=20, valorMin = 1, valorMax = 100, sinRepes = False):
    '''Genera una lista al azar con la cantidad de valores ingresados por parametro,
    y entre los rangos definidos por parametros. Puede o no permitir repetidos.
    
    Devuelve una lista.
    
    Parámetros:
    cantElem -> Cantidad de elementos aleatorios a agregar a la lista (20 por defecto)
    valorMin -> El valor minimo que pueden tener los elementos (1 por defecto)
    valorMax -> El valor maximo que pueden tener los elementos (100 por defecto)
    sinRepes -> Si es verdadero, la lista no tendra elementos repetidos (False por defecto)

    '''
    lista = []
    elemAgregados = 0
    while elemAgregados < cantElem:
        valor = rndm(valorMin, valorMax)
        while sinRepes and valor in lista:
            valor = rndm(valorMin, valorMax)
        lista.append(valor)
        elemAgregados += 1
    
    return lista