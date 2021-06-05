def contarVocalesIterativa(cad):
    '''Cuenta cuantas vocales tiene una cadena en forma iterativa.'''
    cont = 0    
    for letra in cad:
        letra = letra.lower()
        if letra in ['a','e','i','o','u']:
            cont += 1
        else:
            cont += 0
    return cont


def contarVocalesRecursivo(cad):
    '''Cuenta cuantas vocales tiene una cadena en forma recursiva.'''
    #cada iteracion va a analizar un caracter, el primero de la cadena que recibe
    if len(cad)==0:
        return 0
    else:
        letra = cad[0].lower()
        if letra in ['a','e','i','o','u']:
            return 1 + contarVocalesRecursivo(cad[1:]) 
        else:
            return 0 + contarVocalesRecursivo(cad[1:])


def main():
    cadena = input("Ingrese una cadena:")
#     print("Cantidad de vocales Iterativo:", contarVocalesIterativa(cadena))
    print("Cantidad de vocales Recursivo:", contarVocalesRecursivo(cadena))
main()