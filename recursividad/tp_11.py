#obtener el minimo de una fila
#si ese es menor al guardado, quedarmelo
def minimoMatriz(matriz):
    if(len(matriz) == 1):
        return min(matriz[0])
    
    minimo = min(matriz[0])
    minimoSiguiente = minimoMatriz(matriz[1:])
    if(minimo < minimoSiguiente):
        return minimo
    else:
        return minimoSiguiente

def main():
    matriz = [
        [8, 10, 50, 6],
        [3, 20, 33, 0],
        [15, 20, 33, 5],
        [3, 20, 33, 1]
    ]

    minimo = minimoMatriz(matriz)

    print(minimo)
main()