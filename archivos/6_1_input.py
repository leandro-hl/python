#Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo
#una frase y un entero N, y devuelva otra cadena con las palabras que tengan
#N o más caracteres de la cadena original. Escribir también un programa para
#verificar el comportamiento de la misma. Hacer tres versiones de la función, para
#cada uno de los siguientes casos:
#a. Utilizando sólo ciclos normales
#b. Utilizando listas por comprensión
#c. Utilizando la función filter
def filtrar_palabras_ciclo(frase, min_caracteres):
    """
        Version a: ciclos
    """
    palabras = frase.split(' ')
    nuevaFrase = []

    for palabra in palabras:
        if(len(palabra) > min_caracteres):
            nuevaFrase.append(palabra)

    return " ".join(nuevaFrase)

def filtrar_palabras_comprension(frase, min_caracteres):
    """
        Version b: listas por comprensión
    """
    palabras = frase.split(' ')

    return " ".join([palabra for palabra in palabras if len(palabra) > min_caracteres])

def filtrar_palabras_flter(frase, min_caracteres):
    """
        Version c: función filter
        otro comentario
    """
    palabras = frase.split(' ')

    return " ".join(filter(lambda palabra: len(palabra) > min_caracteres, palabras))

def main():
    frase = "Yo tengo un ojo de un color y otro de un color distinto"
    minimo = 2 #agrego un comment

    print(frase)
    print(filtrar_palabras_flter(frase, minimo))
    #comment
main()