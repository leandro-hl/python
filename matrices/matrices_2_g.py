import math as m

def MarcarPerimetro(matriz, n, maximo, minimo, k):
    if(n == 1):
        perimetro = 1
    else:
        perimetro = (n-1)*4
        
    i = j = minimo
    
    for z in range(perimetro):
        matriz[i][j] = k
        k += 1
        
        if(i == minimo and j < maximo - 1):
            j += 1
        elif(j == maximo - 1 and i < maximo -1):
            i += 1
        elif(i == maximo - 1 and j > minimo):
            j -= 1
        elif(j == minimo and i > minimo + 1):
            i -= 1
            
    return k

def NuevoPerimetro(n, maximo, minimo):
    return n - 2, maximo - 1, minimo + 1

def MarcarMatriz():
    n = int(input("Ingrese area de matriz"))

    matriz = [[0] * n for i in range(n)]
    
    niveles = m.ceil(n/2)
    minimo = 0
    maximo = n
    k = 1
    print("niveles: ", niveles)
    
    for i in range(niveles):
        print("n: ",n, " ", "maximo: ", maximo, " ", "minimo: ", minimo)
        
        k = MarcarPerimetro(matriz, n, maximo, minimo, k)
        n, maximo, minimo = NuevoPerimetro(n, maximo, minimo)

    print(matriz)
    
def Main():
    MarcarMatriz()
    
Main()