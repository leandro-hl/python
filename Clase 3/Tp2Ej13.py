# Escribir un programa para generar una lista con los
# múltiplos de 7 que no sean múltiplos de 5, entre 2000 y 3500.
# Imprimir la lista obtenida.

def main():
    lista = []
    for x in range(2000,3501):
        if x % 7 == 0 and x % 5 != 0:
            lista.append(x)
    
    print(lista)
    
    listaComprension = [x for x in range(2000,3501) if x % 7 == 0 and x % 5 != 0]
    
if __name__ == "__main__":
    main()