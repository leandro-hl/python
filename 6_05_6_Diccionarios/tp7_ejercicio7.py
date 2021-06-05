# Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo
# Común Divisor (también llamado Divisor Común Mayor) basándose en las siguientes
# propiedades:
# MCD(X, X) = X
# MCD(X, Y) = MCD(Y, X)
# Si X > Y => MCD(X, Y) = MCD(X–Y, Y).
# Utilizando la función anterior calcular el MCD de todos los elementos de una lista
# de números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
# utilizar iteraciones en ninguna etapa del proceso.


def mcd(x,y):
    '''Retorna el mcd de dos numeros.'''
    
    if x < 0 or y < 0:
        return -1
    
    if x == y:
        return x
    else:
        if x > y :
            return mcd(x-y, y)
        else:
            return mcd(y, x)
 
 
print(mcd(16,8)) 