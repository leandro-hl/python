#Intercambiar posicion 0 y 3 en una lista
lista=[1,2,3,4,5,6]
aux = lista[0]
lista[0] = lista[3]
lista[3] = aux
print(lista)

#Intercambiar Filas (Especifico de Python)
matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
aux = matriz[0]
matriz[0] = matriz[3]
matriz[3] = aux
print(matriz)

#Intercambiar Columnas (General para la mayoria de los lenguajes)
matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for fila in matriz:
    aux = fila[0]
    fila[0] = fila[3]
    fila[3] = aux
print(matriz)

#Intercambiar Filas (0 por 3, por ejemplo)
long=len(matriz)
for j in range(long):
    aux=matriz[0][j]
    matriz[0][j]=matriz[3][j]
    matriz[3][j]=aux
print(matriz)