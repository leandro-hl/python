# Intercambiar filas por columnas
# Solo voy a admitir cambiar filas y columnas con el mismo indice

#Funciones
def intercambiarFilaYColumna(matriz, x):
    for i in range(len(matriz)): # matriz cuadrada
        aux = matriz[x][i]
        matriz[x][i] = matriz[i][x]
        matriz[i][x] = aux
        

matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
intercambiarFilaYColumna(matriz, 1)
print(matriz)

#Transponer matriz
matriz=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

long = len(matriz)
for i in range(long):
    for j in range(i):
        aux = matriz[i][j]
        matriz[i][j] = matriz[j][i]
        matriz[j][i] = aux

for i in range(long):
    print(matriz[i])