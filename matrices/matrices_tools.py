import random as r

def CrearCeroMatrizConArea():
    area = int(input("Ingrese el area de la matriz"))
    
    return [[0] * area for i in range(area)]

def CrearMatrizAMano():
    area = int(input("Ingrese el area de la matriz"))
    matriz = []
    
    for i in range(area):
        matriz.append([])
        
        for j in range(area):
            mensaje = "Ingrese el nro para la posicion: " + str(i) + str(j)
            n = int(input(mensaje))
            matriz[i].append(n)
            
    return matriz

def CrearMatriz():
    area = int(input("Ingrese el area de la matriz"))
    
    matriz = []
    
    for i in range(area):
        matriz.append([])
        
        for j in range(area):
            matriz[i].append(r.randint(1,10))
            
    return matriz
