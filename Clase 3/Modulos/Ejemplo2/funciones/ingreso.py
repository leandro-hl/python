'Funciones relacionadas al ingreso de informacion'

def IngresarPositivo(texto):
    'Solicita el ingreso de un numero entero positivo'
    numero = int(input(texto))
    while numero < 1:
        print("El numero ingresado no es valido.")
        numero = int(input(texto))
    
    return numero
