def sumaElementosIterativa(lista):
    '''Suma los elementos de una lista. Iterativa'''    
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def sumaElementosRecursivo(lista):
    '''Suma los elementos de una lista. Recursivo'''    
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumaElementosRecursivo(lista[1:])







def sumaElementosRecursivoIndice(lista, i=0):
    '''Suma los elementos de una lista. Recursivo'''
    if i ==len(lista):
        return 0
    else:
        return lista[i] + sumaElementosRecursivoIndice(lista, i+1)








def crearLista():
    lista=[]
    nro = int(input("Ingrese un numero (-1 para finalizar):"))
    while nro != -1:
        lista.append(nro)
        nro = int(input("Ingrese un numero (-1 para finalizar):"))
    return lista
              
    
    
def main():
    lista = crearLista()
    print(lista)
#     print("Forma Iterativa, la suma es:",sumaElementosIterativa(lista))
    print("Forma Recursiva, la suma es:",sumaElementosRecursivo(lista))

main()
        
            