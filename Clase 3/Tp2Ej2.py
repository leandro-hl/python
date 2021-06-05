#2. Escribir funciones para:
#  a.  Generar una lista de 50 números aleatorios del 1 al 100.
#  b.  Recibir una lista como parámetro y devolver True si la misma contiene
#      algún elemento repetido. La función no debe modificar la lista.
#  c.  Recibir una lista como parámetro y devolver una nueva lista con los
#      elementos únicos de la lista original, sin importar el orden.

import random

def GenerarListaAleatoria():
    '''Genera una lista de 50 elementos aleatorios entre 1 y 100'''
    lista = []
    for x in range(50):
        lista.append(random.randint(1,100))
    
    return lista

def TieneRepetidos(lista):
    '''Verifica si una lista tiene elementos repetidos'''
    repetido = False
    x = 0
    while x < len(lista):
        y = x + 1
        while y < len(lista):
            if lista[x] == lista[y]: repetido = True
            y += 1           
        x += 1

    return repetido

def TieneRepetidosMejorado(lista):
    '''Verifica si una lista tiene elementos repetidos'''
    repetido = False
    x = 0
    while not repetido and x < len(lista):
        y = x + 1
        while not repetido and y < len(lista):
            if lista[x] == lista[y]: repetido = True
            else: y += 1
        x += 1

    return repetido

def SinRepetidos(lista):
    '''A partir de una lista dada genera una nueva lista sin elementos repetidos'''
    nuevaLista = []
    for n in lista:
        repetido = False
        for m in nuevaLista:
            if n == m: repetido = True
        if not repetido: nuevaLista.append(n)
        
    return nuevaLista

def main():
    lista = GenerarListaAleatoria()
    print("Lista aleatoria")
    print(lista)
    print("TieneRepetidos")
    print(TieneRepetidos(lista))
    print("TieneRepetidosMejorado")
    print(TieneRepetidosMejorado(lista))
    lista2 = SinRepetidos(lista)
    print("Lista sin repetidos")
    print(lista2)
    print("TieneRepetidos")
    print(TieneRepetidos(lista2))
    print("TieneRepetidosMejorado")
    print(TieneRepetidosMejorado(lista2))
    
main()
        