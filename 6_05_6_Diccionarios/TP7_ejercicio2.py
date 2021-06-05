# TP7 - ejercicio 2
# Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.

# 1 0 1 1  -> 1*2**0 + 1*2**1 + 0*2**2 + 1*2**2 + 0
# cada recursividad resuelve un termino

def binarioDecimal(binario, exp=0):
    '''Convertir a decimal.
    Recibe un numero en binario'''
    
    if binario == 0:
        return 0
    else:
        digito = binario % 10
        termino = digito * (2**exp)
        return termino + binarioDecimal(binario//10, exp + 1)
        
        
binario=int(input("ingrese numero binario:"))
print(binario)
print(f"El numero {binario} en decimal: {binarioDecimal(binario)}")
