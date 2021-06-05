# Escribir un programa para generar una lista con los múltiplos de 7 que no sean
# múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.
def EncontrarPrimerMultiplo(minimo, numeroABuscar):
    while minimo % numeroABuscar != 0:
        minimo+=1

    return minimo

def GenerarListaMultiplos():
    minimo = 2000
    maximo = 3500
    numeroABuscar = 7
    numeroAEvitar = 5
    multiplosDeSiete = []

    minimo = EncontrarPrimerMultiplo(minimo, numeroABuscar)

    while minimo <= maximo:

        if(minimo % numeroABuscar == 0 and minimo % numeroAEvitar != 0):
            multiplosDeSiete.append(minimo)

        minimo+=numeroABuscar

    print(multiplosDeSiete)

GenerarListaMultiplos()