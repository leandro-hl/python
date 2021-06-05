# Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
# una lista con los números de las mismas.

def obtenerColumnasCapicua():
    matriz = [[1,2,3,2],
              [2,1,3,2],
              [1,1,3,2]]

    columnasCapicuas = []
    cantColumnas = len(matriz[0])
    filasAEvaluar = len(matriz) // 2

    for columna in range(cantColumnas):
        inicio = 0
        fin = -1
        esCapicua = True

        while esCapicua and inicio < filasAEvaluar:
            if(matriz[inicio][columna] != matriz[fin][columna]):
                esCapicua = False
            else:
                inicio += 1
                fin -= 1

        if(esCapicua):
            columnasCapicuas.append(columna)

    return columnasCapicuas

def Main():
    matriz = []

    columnasCapicuas = obtenerColumnasCapicua(matriz)

    print(columnasCapicuas)
Main()