#Escribir un programa que lea un archivo de texto conteniendo un conjunto de
#apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
#ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
#cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
#ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
#Arslanian, Gustavo –> ARMENIA.TXT
#Rossini, Giuseppe –> ITALIA.TXT
#Pérez, Juan –> ESPAÑA.TXT
#Smith, John –> descartar
#El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
#escribir un programa para generarlo.
def tryOpenFile(file, action):
    try:
        return open(f'2_parcial\\archivos\\{ file }.txt', action)
    except IOError:
        print(f'Error intentando abrir { file }')
    
def ObtenerArchivo(sufijo, sufijos):
    if sufijo in sufijos:
        return sufijos[sufijo]
    return ''

def main():
    sufijos = { 'IAN': 'ARMENIA', 'INI': 'ITALIA', 'EZ': 'ESPAÑA' }

    file = tryOpenFile('6_4_input', 'r')

    if file is not None:
        for registro in file:
            apellido = registro.split(',')[0]

            sufijo = apellido[len(apellido)-3::].upper() 

            archivodestino = ObtenerArchivo(sufijo, sufijos)

            if not archivodestino.isalpha():
                archivodestino = ObtenerArchivo(sufijo[len(sufijo)-2::], sufijos)

            if archivodestino.isalpha():        
                outputFile = tryOpenFile(archivodestino, 'w')

                if outputFile is not None:
                    outputFile.write(registro)
                    outputFile.close()
        file.close()

main()