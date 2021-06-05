#NO PERDER EL TIEMPO CON LOS ACENTOS.
#PREGUNTAS Y AVISO SI LLEGO LA TAREA: HACER A GALATI VERONICA
#Trabajar con la estrctura While-True y generar 
#y capturar excepciones para resolver el siguiente problema:
#Seguimos con contraseñas! En algunos sitios no se permite repetir la contraseña y 
#tampoco tener más de n caracteres iguales, Se solicita un programa para simular “cambiar una contraseña”.
#Como regla general: Las contraseñas no pueden contener espacios y 
#debe tener al menos 10 caracteres, de los cuales al menos dos deben ser números 
#y al menos una mayúscula.
#Ingresar por teclado  contraseña actual y contraseña nueva. 
#Ambas deben cumplir la regla general y además
#Se debe aceptar la nueva contraseña si ésta tiene el 70% diferente a la contraseña actual.
#Permitir simular cambios de contraseña hasta que se ingrese una contraseña vacía en la actual
import math as m

class CaracteresMinimoException(Exception):
    pass

class CaracterInvalidoException(Exception):
    pass

class CantidadNumerosMinimoException(Exception):
    pass

class CantidadMayusculasMinimoException(Exception):
    pass

class CantidadCaracteresDistintosException(Exception):
    pass

def evaluarContrasenia(contrasenia):
    cantidadCaracteresMinimo = 10
    cantidadNumerosMinimo = 2
    cantidadMayusculasMinimo = 1
    caracterInvalido = ' '

    cantidadMayusculasContrasenia = 0
    cantidadNumerosContrasenia = 0

    if(len(contrasenia) < cantidadCaracteresMinimo):
        raise CaracteresMinimoException(contrasenia)
    
    if(contrasenia.find(caracterInvalido) != -1):
        raise CaracterInvalidoException(contrasenia)
    
    for caracter in contrasenia:
        if(caracter.isdigit()):
            cantidadNumerosContrasenia += 1
        elif(caracter.isupper()):
            cantidadMayusculasContrasenia += 1

    if(cantidadMayusculasContrasenia < cantidadMayusculasMinimo):
        raise CantidadMayusculasMinimoException(contrasenia)

    if(cantidadNumerosContrasenia < cantidadNumerosMinimo):
        raise CantidadNumerosMinimoException(contrasenia)

def evaluarContraseniasSonDiferentes(contraseniaVieja, contraseniaNueva):
    """
        Evalua que la nueva contrasenia sea al menos un 70% diferente a la vieja.
        Utiliza math.ceil para redondear hacia arriba la cantidad minima de caracteres diferentes
        (Para mayor seguridad y saber que siempre cumplimos con el 70% minimo)

        Dado que la contraseñas pueden tener caracteres repetidos, iteramos.
        Si no fuera el caso y no importara el orden de los mismos, usariamos diferencia de conjuntos.
    """
    porcentageMinimo = 70

    cantCaracteresContraseniaNueva = len(contraseniaNueva)

    cantCaracteresDiferenciaMinima = m.ceil(porcentageMinimo * len(contraseniaVieja) / 100)
    cantCaracteresDiferentes = 0

    for indice in range(cantCaracteresDiferenciaMinima):
        if(indice >= cantCaracteresContraseniaNueva):
            break

        if(contraseniaVieja[indice] != contraseniaNueva[indice]):
            cantCaracteresDiferentes += 1

    if(cantCaracteresDiferentes < cantCaracteresDiferenciaMinima):
        raise CantidadCaracteresDistintosException

def main():
    while True:
        contraseniaVieja = input('Ingrese su contraseña anterior:\n')

        if(contraseniaVieja == ''):
            break

        contraseniaNueva = input('Ingrese su contraseña nueva:\n')

        try:
            evaluarContrasenia(contraseniaVieja)
            evaluarContrasenia(contraseniaNueva)
            evaluarContraseniasSonDiferentes(contraseniaVieja, contraseniaNueva)
    
            print("Contraseña actualizada con exito!")
        except CaracteresMinimoException as mje:
            print(f'La contraseña: { mje.args[0] } no cumple con la cantidad minima de caracteres requeridos')
        
        except CaracterInvalidoException as mje:
            print(f'La contraseña: { mje.args[0] } no puede tener caracteres invalidos')

        except CantidadNumerosMinimoException as mje:
            print(f'La contraseña: { mje.args[0] } no puede tener menos numeros de los requeridos')

        except CantidadMayusculasMinimoException as mje:
            print(f'La contraseña: { mje.args[0] } no puede tener menos mayusculas de las requeridas')

        except CantidadCaracteresDistintosException as mje:
            print(f'La contraseña: { contraseniaNueva } no cumple con la cantidad minima de caracteres distintos a la contraseña anterior: { contraseniaVieja }')

        except Exception:
            print("Ocurrio un error inesperado. Vuelva a intentar.")
main()