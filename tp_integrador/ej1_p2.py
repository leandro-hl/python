
import tools as t 
import random as r

# Crear una  lista al  azar,  luego informar  para  cada  valor,  
# cuántas  veces  se repite(Utilizar el métodocount). El informe no debe repetir el número.

#Funciones
def EliminarOcurrenciasValorInformado(lista, numeroInformado, cantidadVeces):
    for j in range(cantidadVeces):
        lista.remove(numeroInformado)

def InformarValor(lista):
    numeroAContar = lista[0]
    cantidadVeces = lista.count(numeroAContar)

    print("El numero: ", numeroAContar, " aparece ", cantidadVeces, " vez en la lista")

    EliminarOcurrenciasValorInformado(lista, numeroAContar, cantidadVeces)

def GenerarInforme(lista):
    while lista != []:
        InformarValor(lista)

#Programa Principal
def Main():
    cantidadElementos = r.randint(1, 100)

    lista = t.CrearLista(True, cantidadElementos)
    
    t.OrdenarDescendentementeListaNumerica(lista)

    print("Lista creada: ", lista)

    GenerarInforme(lista)

Main()