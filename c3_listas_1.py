def CrearListaCuadrados(n):
    lista = []
    
    for x in range(1, n+1):
        lista.append(x**2)
        
    return lista

def ImprimirUltimos10(lista):
    
    if len(lista) >= 10:
        hasta = -10
    else:
        hasta = -len(lista)
        
    for x in range(-1, hasta-1): #xq estoy yendo para atras
        print(lista[x], end=",")
        
def main():
    n = 20
    lista = CrearListaCuadrados(n)    
    ImprimirUltimos10(lista)
    
if __name__ == "main"
    main()