# Desarrollar un programa para eliminar todos los comentarios de
# un programa escrito en lenguaje Python. Tener en cuenta que los
# comentarios comienzan con el signo # (siempre que éste no se
# encuentre encerrado entre comillas simples o dobles) y que también
# se considera comentario a las cadenas de documentación (docstrings).

# Eliminando solo comentarios simples (de una linea):
# instruccion # comentario -> instruccion
# # comentario solo -> linea en blanco

def main():
    strArch = input("Ingrese nombre de archivo .py (Sin la extensión): ")
    try:
        archOrigen = open(strArch + ".py","r")
        archDestino = open(strArch + "-NoComments.py","w")
    except IOError:
        print(f"No pudo abrirse el archivo {strArch}.py o hubo un error al crear el archivo {strArch}-NoComments.py")
    else:
        for linea in archOrigen:
            if "#" in linea:
                archDestino.write(linea[:linea.index("#")].rstrip(" ")+"\n")
            else:
                archDestino.write(linea)
        archOrigen.close()
        archDestino.close()

if __name__ == "__main__":
    main()