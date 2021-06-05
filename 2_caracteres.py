#Cree
#un programa que ingrese primero el apellido y a continuación el nombre,
#deberá crear una cadena que contenga Apellido una coma un espacio y el
#Nombre (si tiene doble apellido o doble nombre, debe quedar con un solo
#espacio entre cada palabra) Luego se solicita que lo muestre por pantalla
#centrado (Considerando una pantalla con 80 columnas de ancho) y alternando
#mayúsculas y minúsculas por palabra Ejemplo Martinez Juan Pedro
#MaRtInEz, JuAn PeDrO

def main():
    apellido = "Martinez"
    nombre = "Juan Pedro"

    nombreYApellido = apellido + ", " + nombre

    print(nombreYApellido)

    output = ""
    for index, caracter in enumerate(nombreYApellido):
        if caracter.isalpha() and index%2 == 0:
            output += caracter.upper()
        else:
            output += caracter.lower()

    print(output)
main()