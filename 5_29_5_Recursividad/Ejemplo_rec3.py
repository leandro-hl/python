def factorialRecursivo(n):
    '''Retorna el factorial de n o -1 si es negativo.'''
    if n ==0 or n == 1:
        return 1
    elif n<0:
        return -1
    else:
        return n * factorialRecursivo(n-1)

def factorialIterativo(n):
    '''Retorna el factorial de n o -1 si es negativo.'''
    if n<0:
        factorial = -1
    else:
        factorial=1
        for cont in range(1,n+1):
             factorial = factorial * cont
    return factorial



print(factorialRecursivo(4))