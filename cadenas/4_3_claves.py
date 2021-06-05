#Los números de claves de dos cajas fuertes están intercalados dentro de un número
#entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
#para obtener ambas claves, donde la primera se construye con los dígitos
#impares de la clave maestra y la segunda con los dígitos pares. Los dígitos se
#numeran desde la izquierda. Ejemplo: Si clave maestra = 18293, la clave 1 sería
#123 y la clave 2 sería 89.

def main():
    claveMaestra = "18293"
    
    clavePrimaria = claveMaestra[::2]
    claveSecundaria = claveMaestra[1::2]

    print(f"clave primaria { clavePrimaria }")
    print(f"clave secundaria { claveSecundaria }")

main()