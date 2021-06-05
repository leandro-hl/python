# Ejercicio 3: Realizar un programa para ingresar desde el teclado un conjunto de números e
# informar si la cantidad de elementos es impar o par, sin utilizar contadores.
# Finalizar la lectura de datos con el valor -1.

def UsandoListas():
    mensaje = "Ingrese un numero"
    n = int(input(mensaje))
    
    numeros = []
    while n != -1:
        numeros.append(n)
        n = int(input(mensaje))
        
    esPar = len(numeros) % 2 == 0
    
    print("Es par: ", esPar)
    
def Main():
    mensaje = "Ingrese un numero"
    n = int(input(mensaje))

    esPar = True

    while n != -1:
        if(esPar):
            esPar = False
        else:
            esPar = True
        
        n = int(input(mensaje))
    
    print("Es par: ", esPar)
    
Main()