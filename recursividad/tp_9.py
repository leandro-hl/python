def crearMatriz(n):
    matriz = []

    for i in range(n):
        matriz.append([])

        for j in range(n):
            matriz[i].append(j)

def imprimirColumna(columna):
    print(columna)

def imprimirFila(fila):
    if(len(fila) == 0):
        return 

    imprimirColumna(fila[0])

    imprimirFila(fila[1:])

def imprimirMatriz(matriz):
    if(len(matriz) == 0):
        return       
    
    imprimirFila(matriz[0])

    imprimirMatriz(matriz[1:])

def main():
    matriz = [
        [0, 1, 2],
        [2, 1, 0]
    ]

    imprimirMatriz(matriz)
main()