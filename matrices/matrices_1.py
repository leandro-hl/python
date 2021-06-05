import random as r
import matrices_tools as tool

def OrdenarMatriz(matriz):
    for i in range(len(matriz)):
        OrdenarFila(matriz[i])
        
    print("matriz ordenada: ", matriz)

def OrdenarFila(fila):
    for i in range(len(fila)):
        for j in range(i, len(fila)):
            actual = fila[i]
            proximo = fila[j]
            
            if(proximo > actual):
                fila[i] = proximo
                fila[j] = actual

    print("fila ordenada: ", fila)

def IntercambiarFilas(matriz, nroFila1 = 0, nroFila2 = 0):
    aux = matriz[nroFila1]
    
    matriz[nroFila1] = matriz[nroFila2]
    matriz[nroFila2] = aux
    
    print("matriz con fila: ", nroFila1, " cambiada por fila: ", nroFila2, " : ", matriz)

def IntercambiarColumnas(matriz, nroCol1 = 0, nroCol2 = 0):
    
    for i in range(len(matriz)):        
        fila = matriz[i]
        
        aux = fila[nroCol1]
        fila[nroCol1] = fila[nroCol2]
        fila[nroCol2] = aux
    
    print("matriz con columna: ", nroCol1, " cambiada por columna: ", nroCol2, " : ", matriz)

def IntercambiarFilaYColumna(matriz, filaColumnaACambiar):
    columna = []
    fila = matriz[filaColumnaACambiar]
    
    for i in range(len(matriz)):
        columna.append(matriz[i][filaColumnaACambiar])

        matriz[i][filaColumnaACambiar] = fila[i]
        
    matriz[filaColumnaACambiar] = columna
    
    print("matriz con fila: ", filaColumnaACambiar, " cambiada por columna: ", filaColumnaACambiar, " : ", matriz)

def TransponerMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    
    print("matriz transpuesta: ", matriz)
    
def Main():
    print()
    
    #matriz = CrearMatrizAMano()
    matriz = tool.CrearMatriz()
    
    OrdenarMatriz(matriz)
    
    filaACambiar = r.randint(0, len(matriz)-1)
    filaACambiar2 = r.randint(0, len(matriz)-1)
    
    IntercambiarFilas(matriz, filaACambiar, filaACambiar2)
    
    columnaACambiar = r.randint(0, len(matriz)-1)
    columnaACambiar2 = r.randint(0, len(matriz)-1)
    
    IntercambiarColumnas(matriz, columnaACambiar, columnaACambiar2)
    
    filaColumnaACambiar = r.randint(0, len(matriz)-1)
    
    IntercambiarFilaYColumna(matriz, filaColumnaACambiar)
    
    TransponerMatriz(matriz)
Main()
