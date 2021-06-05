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
    for fila in matriz:
        cont += fila.count(valor)
    return cont

def contarRecursivo(matriz,valor):
    if len(matriz) == 0:
        return 0
    else:
        return matriz[0].count(valor) + contarRecursivo(matriz[1:],valor)


def main():
    m = crearMatriz(4)
    print("Matriz creada:")
    for fila in m:
        print(*fila)
    valor = int(input("Ingrese el valor a contar:"))    
#     print(f"Forma Iterativa {valor} aparece {contarIterativo(m,valor)}")
    
    print(f"Forma Recursiva {valor} aparece {contarRecursivo(m,valor)}")
    
main()
        