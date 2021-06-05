import random as r 

# Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
# auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].0,1,2,3,4

def EsCapicua(lista):
    fin = -1
    cantElementos = len(lista)
    esCapicua = True

    iteraciones = cantElementos // 2

    if(cantElementos % 2 == 0):
        iteraciones += 1

    for i in range(iteraciones):
        if(lista[i] != lista[fin]):
            esCapicua = False
        
        fin -=1

    return esCapicua

def Main():
    largoLista = int(input("Ingrese Largo lista"))

    lista = []
    for i in range(largoLista):
        lista.append(int(input("Ingrese nro lista")))

    print("su lista: ", lista)
    print(EsCapicua(lista))


Main()