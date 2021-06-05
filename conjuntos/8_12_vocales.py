#Crear una función, que reciba una palabra y cuente cuántas letras
#"a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario con los resultados.
#Desarrollar un programa para leer una frase e invocar a la función por cada
#palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales
#hallada.

def contarvocales(palabra):
    vocales = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }

    palabra = palabra.lower()
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1

    return vocales

def main():
    frase = "tres tristes tigres comen trigo en tres trigales"

    for palabra in frase.split():
        conteoVocales = contarvocales(palabra)

        print(f'La palabra: { palabra } tiene { sum(conteoVocales.values()) } vocales')

main()