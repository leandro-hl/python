import matrices_tools as tool

def MatrisEsSimetrica(matriz, esDiagonalPrincipal):
    esSimetrica = True
    area = len(matriz)
    
    if(esDiagonalPrincipal):
        for i in range(area):
            for j in range(i):
                if(esSimetrica and j != i and matriz[i][j] != matriz[j][i]):
                    esSimetrica = False
    else:
        for i in range(area, 0, -1):
            for j in range(area-i):
                if(esSimetrica and i != j):
                    iAEvaluar = area - (i + 1)
                    jAEvaluar = area - (j + 1)
                    
                    if(matriz[i][j] != matriz[iAEvaluar][jAEvaluar]):
                        esSimetrica = False
    
    print("La matriz es simetrica: ", esSimetrica)         

def Main():
    print()
    
    #matriz = CrearMatrizAMano()
    matriz = tool.CrearMatriz()
    
    esDiagonalPrincipal = False
    MatrisEsSimetrica(matriz, esDiagonalPrincipal)

Main()