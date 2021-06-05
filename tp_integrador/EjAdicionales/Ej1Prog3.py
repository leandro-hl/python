# Programa 3: Crear una lista al azar sin elementos repetidos (de 3 digitos). Ordenar según el dígito central
# de los números cargados en la lista. Utilizar metodo sort y el parámetro key para indicar el
# ordenamiento solicitado.
import FnGenLst

def cantDigitos(nro):
    '''Calcula la cantidad de dígitos de un numero'''
    cant = 0
    while nro > 0:
        nro = nro // 10
        cant += 1
    return cant

def digitoCentral(nro):
    '''Devuelve el dígito central de un numero'''
    for i in range(cantDigitos(nro)//2):
        nro = nro // 10
    return nro % 10

def main():
    lista = FnGenLst.generarLista(20, 100, 999, sinRepes=True)
    print(lista)
    lista.sort(key=digitoCentral)
    print(lista)

if __name__ == "__main__": 
    main()