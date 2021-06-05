def sumaNaturalesIterativo(n):
    '''Suma los N primeros numeros naturales en forma iterativa.'''
    suma=0
    for cont in range(n+1):
        suma=suma+cont
    return suma

def sumaNaturalesRecursivo(n):
    '''Suma los N primeros numeros naturales en forma recursiva.'''
    if n < 0:
        return -1
    elif n==0:
        return 0
    else:
        return n + sumaNaturalesRecursivo(n-1)   
    
def ingresarNatural():
    '''Solicita el ingreso de un numero natural utilizando excepciones.'''
    while True:
        try:
            nro = int(input("Ingrese un numero natural: "))
            if nro < 1:
                print("Error, se solicita un numero natural")
                continue
        except ValueError:
            print("Error, se solicita un numero natural")
        else:
            break;
    return nro

#PROGRAMA PRINCIPAL
def main():
    n=ingresarNatural()
    print("En forma iterativa:", sumaNaturalesIterativo(n))
    print("En forma recursiva:",sumaNaturalesRecursivo(n))

if __name__ == "__main__":    
    main()
    