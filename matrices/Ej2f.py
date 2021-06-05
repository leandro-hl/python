N=4

matriz = []
for f in range(N):
    matriz.append([None]*N)

k = 1
for i in range(N):
    for j in range(N-1,-1,-1):
        if (j >= N-1-i):
            matriz[i][j] = k
            k += 1
        else:
            matriz[i][j] = 0

for i in range(N):
    print(matriz[i])