# Desarrollar un programa para eliminar todos los comentarios de
# un programa escrito en lenguaje Python. Tener en cuenta que los
# comentarios comienzan con el signo # (siempre que éste no se
# encuentre encerrado entre comillas simples o dobles) y que también
# se considera comentario a las cadenas de documentación (docstrings).

# Eliminando comentarios simples:
# instruccion # comentario -> instruccion
# # comentario solo -> elimino la linea
# Teniendo en cuenta casos mas complicados:
# print("Este texto tiene un #") # y un comentario -> print("Este texto tiene un #")

def main():
    strArch = input("Ingrese nombre de archivo .py (Sin la extensión): ")
    try:
        archOrigen = open(strArch + ".py","r")
        archDestino = open(strArch + "-NoComments.py","w")
    except IOError:
        print(f"No pudo abrirse el archivo {strArch}.py o hubo un error al crear el archivo {strArch}-NoComments.py")
    else:
        for linea in archOrigen:
            if linea.lstrip(" ")[0] != "#": # Ignoro las lineas que empiezan con #
                desde = 0
                linea.replace("\n","")
                while "#" in linea[desde:]:
                    hasta = linea.index("#", desde)
                    
                    posDoble = linea.find("\"", desde) 
                    posSimple = linea.find("\'", desde)
                    hayComillas = False
                    
                    # Si encuentro comillas simples y, o estan antes que las dobles o no hay dobles:
                    if posSimple > -1 and (posSimple < posDoble or posDoble == -1):
                        comilla = "\'"
                        posComilla = posSimple
                        hayComillas = True
                    # Sino, si encuentro comillas dobles:
                    elif posDoble > -1:
                        comilla = "\""
                        posComilla = posDoble
                        hayComillas = True
                        
                    # Si se abrieron comillas antes del asterisco:
                    if hayComillas and linea.count(comilla, desde, hasta) >= 1:
                        # Busco donde se cierran esas comillas
                        desde = linea.index(comilla, posComilla + 1) + 1
                    else:
                        # El asterisco era inicio de comentario, lo elimino
                        linea = linea[:hasta].rstrip(" ")
                archDestino.write(linea + "\n")                
        archOrigen.close()
        archDestino.close()

if __name__ == "__main__":
    main()