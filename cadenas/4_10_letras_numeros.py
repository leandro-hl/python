#Escribir un programa que permita ingresar una cadena de caracteres e imprima un
#mensaje indicando cuántas letras y cuántos números contiene. Por ejemplo, si se
#ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números.

def main():
    frase = "Hola Mundo 123"
    digitos = 0
    alpha = 0
    for letra in frase:
        if(letra.isdigit()):
            digitos+=1
        elif (letra.isalpha()):
            alpha+=1

    print(f"cantidad digitos: { digitos }")
    print(f"cantidad letras: { alpha }")
main()