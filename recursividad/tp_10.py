def sumarMatriz(matriz):
    if(len(matriz) == 0):
        return 0
    
    return sum(matriz[0]) + sumarMatriz(matriz[1:])

def main():
    matriz = [
        [0, 1, 2],
        [2, 1, 0]
    ]

    sumaTotal = sumarMatriz(matriz)

    print(sumaTotal)
main()