# TP7 ejercicio 4
# Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.

# 2 * 3 = 3 + 3

#Funciones

 

def MultiplicacionRecursiva(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return y + MultiplicacionRecursiva(x-1,y)

 

def Main():
    x = int(input("Ingrese un número positivo: "))
    y = int(input("Ingrese otro número positivo: "))
    solucion = MultiplicacionRecursiva(x,y)
    print (f"El resultado del producto entre {y} y {x} es {solucion}")
    
#Programa
Main()