# hacer el 13 por comprension
# Escribir un programa para generar una lista con los múltiplos de 7 que no sean
# múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.

def listaPorComprension():
    lista =  [i for i in range(2002, 3500, 7) if i % 5 != 0]

    print(lista)

listaPorComprension()