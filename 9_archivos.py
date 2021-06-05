#Crear un programa para informar una nota
#y la cantidad de alumnos procesando la informacion
#que se encuentra en el archivo creado en el ejercicio 3
#El
#informe debe mostrar todas las notas

def main():
    try:
        open(r'\2_parcial\ejercicios_clase9\notas.txt')
    except IOError:
        print("Error al abrir archivo")
    else:
        print("Error al abrir archivo")


main()