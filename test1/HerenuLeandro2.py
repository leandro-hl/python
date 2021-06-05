#Plegado de un texto. Escribir una función que ingrese por teclado una longitud 
#y lea de un archivo un texto "texto.txt" que contiene 
#varias oraciones en la mismo o diferente registro.
#Se solicita crear un nuevo archivo "plegado.txt" 
#que contenga una oración por renglón o hasta la longitud máxima indicada, 
#las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras).
#Todas las oraciones finalizan con un punto.
#Informar al finalizar para cada palabra cuántas veces aparece en todo el texto, 
#ordenadas alfabéticamente sin considerar símbolos para el informe.
def palabraSinSimbolos(palabra):
    palabraSinSimb = ''
    for caracter in palabra:
        if(caracter.isalpha()):
            palabraSinSimb += caracter

    return palabraSinSimb

def leerLongitudMaximaCaracteresLinea():
    return int(input("Ingrese la longitud maxima de caracteres por linea que desea."))

def inputNoVacio(input):
    return input != ''

def obtenerPuntoDeCorteOracion(longitudMaximaLinea, oracion):
    """
        Retorna el punto de corte de la oracion cuando se supera la longitud maxima de linea,
        para que la ultima palabra no sea cortada.
        resultado: -1 si no se encontro punto de corte
    """
    ubicacionProximoEspacio = oracion[longitudMaximaLinea:].find(' ')

    if(ubicacionProximoEspacio == -1):
        return -1

    return ubicacionProximoEspacio + longitudMaximaLinea

def grabarOracionEnArchivo(archivo, oracion, longitudMaximaLinea):
    """
        Graba la oracion en el archivo indicado por parametro.
        Corta la oracion segun la longitud maxima indicada.
        No contempla tratamiento de simbolos, dado que no estaba indicado para este caso.
    """
    if(len(oracion) > longitudMaximaLinea):
        puntoCorteOracion = obtenerPuntoDeCorteOracion(longitudMaximaLinea, oracion)
        
        #Si no existe un espacio para realizar el corte, grabamos la oracion completa.
        if(puntoCorteOracion != -1):
            oracion = oracion[:puntoCorteOracion]

    #grabamos en archivo destino
    archivo.write(oracion + '\n')

def grabarAparicionDePalabras(aparicionDePalabras, oracion):
    palabras = oracion.split()
    for palabra in palabras:
        palabra = palabraSinSimbolos(palabra)

        if(inputNoVacio(palabra)):
            if(palabra in aparicionDePalabras):
                aparicionDePalabras[palabra] += 1
            else:
                aparicionDePalabras[palabra] = 1

def informarAparicionTotalDePalabras(aparicionDePalabras):
    """
        Informa la aparicion total de cada palabra encontrada, ordenadas alfabeticamente.
    """

    #Guardamos los items como tuplas en una lista para poder ordenarlos.
    #Otra opcion seria guardar solo las keys pero me parecio mas ordenado de esta forma.
    #Obtenemos el primer item de la tupla (la key) y la pasamos a lower() para su comparacion
    #Si no hacemos esto, tal lo hablado en clase, las palabras con mayusculas van primero
    #en el ordenamiento.
    listaPalabrasYApariciones = list(aparicionDePalabras.items())

    listaPalabrasYApariciones.sort(key=lambda tupla: tupla[0].lower())

    for palabraYAparicion in listaPalabrasYApariciones:
        print(f'La palabra: "{ palabraYAparicion[0] }" aparece en el texto { palabraYAparicion[1] } veces.')

def analizarArchivos(texto, plegado):
    longitudMaximaLinea = leerLongitudMaximaCaracteresLinea()

    aparicionDePalabras = {}

    for registro in texto:
        registro = registro.rstrip("\n")

        oraciones = registro.split('.')

        for oracion in oraciones:
            oracion = oracion.strip(' ')

            if(inputNoVacio(oracion)):
                grabarOracionEnArchivo(plegado, oracion, longitudMaximaLinea)
                grabarAparicionDePalabras(aparicionDePalabras, oracion)

    informarAparicionTotalDePalabras(aparicionDePalabras)    

def main():
    try:
        texto = open('texto.txt')
        plegado = open('plegado.txt', 'w')
    except IOError:
        print("Error al intentar abrir archivos.")
    else:
        try:
            analizarArchivos(texto, plegado)
        except Exception as mje:
            print(f"Ocurrio un error al analizar los archivos. Error { mje }.")
        finally:
            texto.close()
            plegado.close()
main()