import random

def crearMatriz(n,desde=10,hasta=30):
    '''Crea una matriz cuadrada con desde y hasta valores.'''
    matriz=[]
    
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(desde,hasta))
    return matriz
              
def contarIterativo(matriz,valor):
    cont = 0
    suma = 0
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] == valor:
                cont += 1
    return cont

def contarRecursivo(matriz,valor, f=0):
    if f == len(matriz):
        return 0
    else:
        #recorro toda una fila:
        sumaFila=0
        for c in range(len(matriz[f])):
            if matriz[f][c] == valor:
                sumaFila += 1
        return sumaFila + contarRecursivo(matriz,valor, f+1)


def contarTodoRecursivo(matriz,valor, f=0, c=0):
    if f == len(matriz):
        return 0
    else:
        if c == len(matriz[f]):
            return 0 + contarTodoRecursivo(matriz,valor, f+1)
        else:
            #si corresponde sumo un elemento
            if matriz[f][c] == valor:
                return 1 + contarTodoRecursivo(matriz,valor, f, c+1)
            else:
                return 0 + contarTodoRecursivo(matriz,valor, f, c+1)
        
def main():
    m = crearMatriz(4)
    print("Matriz creada:")
    for fila in m:
        print(*fila)
    valor = int(input("Ingrese el valor a contar:"))    
    print(f"Forma Iterativa {valor} aparece {contarIterativo(m,valor)}")
    
    print(f"Forma Recursiva {valor} aparece {contarTodoRecursivo(m,valor)}")
    
main()
        