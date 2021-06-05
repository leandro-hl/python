# TP7 - ejercicio 1
# Escribir una función que devuelva la cantidad de dígitos de un número entero,
# sin utilizar cadenas de caracteres.

# CASO BASE num < 10 retorna 1

def contarDigitos(num):
    ''' Retorna la cantidad de digitos de num.'''
    if num < 0:
        num = -num  # num = num * (-1) 
    
    if num < 10:
        return 1
    else:
        return 1 + contarDigitos(num//10)
 
 
num=-347 
print(f"el numero {num} tiene {contarDigitos(num)} digitos")

