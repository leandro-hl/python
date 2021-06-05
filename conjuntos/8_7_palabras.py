#Ingresar una frase desde el teclado y eliminar las palabras repetidas, dejando un
#solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su
#longitud. La eliminación de las palabras duplicadas debe realizarse a través de un
#conjunto.

def main():
    frase = "tres tristes tigres comen trigo en tres trigales"

    palabras = list(set(frase.split()))

    palabras.sort(key=lambda x: len(x))

    print(palabras)

main()