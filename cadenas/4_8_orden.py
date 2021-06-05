#Escribir una función que reciba como parámetro una cadena de caracteres en la
#que las palabras se encuentran separadas por uno o más espacios. Devolver otra
#cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada
#una.

def ordenarAlfabeticamente(palabras):
    palabras.sort()

def obtenerPalabras(frase):
    return frase.split()

def main():
    frase = "yo  tengo un ojo de un color  y otro de un color distinto"

    palabras = obtenerPalabras(frase)
    print(palabras)

    ordenarAlfabeticamente(palabras)

    print(palabras)
main()