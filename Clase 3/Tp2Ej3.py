#3.  Crear una lista con los cuadrados de los números entre 1 y N
#    (ambos incluidos), donde N se ingresa desde el teclado.
#    Luego se solicita imprimir los últimos 10 valores de la lista.

def CrearListaCuadrados(n):
    lista=[]
    for x in range(1,n+1):
        lista.append(x**2)
    
    return lista

def ImprimirUltimos10(lista):
    if len(lista) >= 10:
        desde = -10
    else:
        desde = -len(lista)
    for x in range(desde,0):
        if x < -1: print(lista[x], end=",")
        else: print(lista[x])
        
def main():
    N = int(input("Cantidad de numeros: "))
    lista = CrearListaCuadrados(N)
    ImprimirUltimos10(lista)
    
main()