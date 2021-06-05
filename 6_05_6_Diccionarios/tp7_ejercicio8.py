# Realizar la implementación recursiva del método de selección para ordenar una
# lista de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
# posición, y luego ordenar el resto de la lista con una llamada recursiva.



def seleccion(lista, i=0):
    '''Ordena una lista.'''
    if len(lista)-1 != i:
        
        #busco la pos del menor elemento de una lista.
        posMin= lista.index(min(lista[i:]))
        
        #intercambiarlo con el elemento que indica i
#         aux = lista[posMin]
#         lista[posMin] = lista[i]
#         lista[i]= aux

        lista[posMin],lista[i] = lista[i],lista[posMin] 

        #vuelvo a llamar a seleccion con el indice uno mas para ordenar el resto de la lista.
        seleccion(lista, i + 1)
        
        
lista=[23,11,24,18,20]
print("creada:",lista)
seleccion(lista)
print("Ordenada",lista)
