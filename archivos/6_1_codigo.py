#Desarrollar un programa para eliminar todos los comentarios de un programa escrito
#en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
#signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
#y que también se considera comentario a las cadenas de documentación
#(docstrings).

def main():
    #abrir archivo 6_1_input.py
    #leer lineas que no empiezan con # 
    #leer lineas que no empiezan con """
    #si la linea contiene un # que no esta entre comillas "" o ''
        #eliminar todo lo que sigue del #
    try:
        inputFile = open(r'D:\Users\Public\Documents\Study\UADE\3_Programacion_I\2_parcial\archivos\6_1_input.py')
        outputFile = open(r'D:\Users\Public\Documents\Study\UADE\3_Programacion_I\2_parcial\archivos\6_1_output.py', mode='w')
    except ValueError:
        print("Error al querer abrir el archivo")
    else:
        comentario = "#"
        docstring = '"""'
        removeDocStringLine = False

        for line in inputFile:
            #eliminar lineas de comentarios
            if(line.startswith(comentario)):
                continue
            
            #eliminar lineas de docstrings
            docStringStart = line.find(docstring)
            docStringEnd = line.rfind(docstring)
            isdocStringStart = docStringStart != -1
            isdocStringEnd = docStringEnd != -1
            isdocStringDiff = docStringStart != docStringEnd

            if(isdocStringStart and isdocStringEnd and isdocStringDiff):
                continue

            if(isdocStringStart and not removeDocStringLine):   
                removeDocStringLine = True
                continue

            if(not isdocStringStart and removeDocStringLine):
                continue

            if(isdocStringStart and removeDocStringLine):   
                removeDocStringLine = False
                continue
            #analizar comentarios en codigo
            posicionComentario = line.find(comentario)

            if(posicionComentario != -1):
                #la linea tiene comentario a eliminar
                line = line[:posicionComentario]
            
            outputFile.write(line)
        
        inputFile.close()
        outputFile.close()

main()