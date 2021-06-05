# Generar matriz:
def generarMatriz():
    n = 4
    numerador = 1
    matriz = [[0 for j in range(n)] for i in range(n)]

    hasta = -2
    inicio = -1
    for fila in range(n):
        
        for columna in range(inicio, hasta, -1):
            matriz[fila][columna] = numerador
            numerador += 1

        hasta -= 1

    print(matriz)

generarMatriz()