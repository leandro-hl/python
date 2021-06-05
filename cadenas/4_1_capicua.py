def esCapicua(cadena):
    largo = len(cadena)
    mitad = largo // 2

    if(largo % 2 == 0):

        return cadena[:mitad] == cadena[:mitad-1:-1]
    else:
        return cadena[:mitad] == cadena[:mitad:-1]

def main():
    cadena = "Yo tengo un ojo de un color y otro de un color distinto"
    palabras = cadena.split()

    for palabra in palabras:
        if(esCapicua(palabra)):
            print(f"La palabra { palabra } es capicua.")
        else:
            print(f"La palabra { palabra } no es capicua.")
main()