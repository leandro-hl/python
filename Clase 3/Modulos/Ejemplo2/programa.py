#Programa Principal
import funciones.ingreso
from funciones.listas import GenerarListaRandom

cantidad = funciones.ingreso.IngresarPositivo("Ingrese un numero: ")
lista = GenerarListaRandom(cantidad)
print("La lista generada es:")
print(lista)

