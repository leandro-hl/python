def ordenadaAscendenteIterativa(lista):
    '''Retorna True si esta ordenada en forma ascendente, False caso contrario. Iterativa'''    
    i=0
    while i< len(lista) -1 and lista[i] < lista[i+1]:
        i += 1
    if i == len(lista)-1:
        return True
    else:
        return False





def ordenadaAscendenteRecursiva(lista):
    '''Retorna True si esta ordenada en forma ascendente, False caso contrario. Recursiva'''
    if len(lista) < 2:
        return True
    else:
        if lista[0] < lista[1]:
            return ordenadaAscendenteRecursiva(lista[1:])
        else:
            return False




def crearLista():
    lista=[]
    nro = int(input("Ingrese un numero (-1 para finalizar):"))
    while nro != -1:
        lista.append(nro)
        nro = int(input("Ingrese un numero (-1 para finalizar):"))
    return lista
              
    
    
def main():
    lista = crearLista()
#     print("Forma Iterativa")
#     if ordenadaAscendenteIterativa(lista) == True:
#         print("La lista esta ordenada en forma ascendente")
#     else:
#         print("La lista No esta ordenada en forma ascendente.")

    print("Forma Recursiva")
    if ordenadaAscendenteRecursiva(lista) == True:
        print("La lista esta ordenada en forma ascendente")
    else:
        print("La lista No esta ordenada en forma ascendente.")

main()
        