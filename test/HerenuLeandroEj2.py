#Desarrollar un programa para que cree 
#un conjunto de N elementos al azar 
#entre A y B (N,A y B puede solicitarlos por teclado o crearlos al azar) 
#Mostrar el conjunto creado por pantalla y 
#luego informe la suma de sus elementos utilizando 
#exclusivamente una función recursiva para sumar los valores.
import random as r 

def crearConjunto():
    #dado que no hay restricciones para los numeros creados, seteamos valores
    #que no requieren muchas validaciones y son faciles de testear
    cantidadElementosConjunto = r.randint(0, 100)
    numeroDesde = r.randint(0, 20)
    numeroHasta = r.randint(21, 40)

    conjunto = set({})

    for i in range(cantidadElementosConjunto):
        ingresarAConjunto = r.randint(numeroDesde, numeroHasta)
        
        if(ingresarAConjunto not in conjunto):
            conjunto.add(ingresarAConjunto)
        else:
            i -= 1

    return conjunto

def mostrarConjunto(conjunto):
    mensaje = ' El Conjunto Creado Es '
    mensaje.center(len(mensaje) + 6, '*')

    print(mensaje)
    print(conjunto)

def sumarConjunto(conjunto):
    if(len(conjunto) == 0):
        return 0
    
    return conjunto.pop() + sumarConjunto(conjunto)

def mostrarSumaValoresConjunto(conjunto):
    suma = sumarConjunto(conjunto)

    print(f'La suma de los valores del conjunto es: { suma }')

def main():
    conjunto = crearConjunto()

    mostrarConjunto(conjunto)
    mostrarSumaValoresConjunto(conjunto)

main()