def filtrar_palabras_ciclo(frase, min_caracteres):
    palabras = frase.split(' ')
    nuevaFrase = []

    for palabra in palabras:
        if(len(palabra) > min_caracteres):
            nuevaFrase.append(palabra)

    return " ".join(nuevaFrase)

def filtrar_palabras_comprension(frase, min_caracteres):
    palabras = frase.split(' ')

    return " ".join([palabra for palabra in palabras if len(palabra) > min_caracteres])

def filtrar_palabras_flter(frase, min_caracteres):
    palabras = frase.split(' ')

    return " ".join(filter(lambda palabra: len(palabra) > min_caracteres, palabras))

def main():
    frase = "Yo tengo un ojo de un color y otro de un color distinto"
    minimo = 2 
    print(frase)
    print(filtrar_palabras_flter(frase, minimo))
    main()