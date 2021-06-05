#Escribir un programa que lea un archivo de texto conteniendo el siguiente formato:
#legajo;apellido;nombre;nota1;nota2
#genere un nuevo archivo agregando al registro la condicion en la que se encuentra: condicion.txt 
#agregando un campo mas indicando cuál debe recuperar: PRIMERO, SEGUNDO, AMBOS o FINAL
#En el nuevo archivo tanto el nombre como el apellido de estar sólo en mayúscula la primera letra.
#Se encuentra un archivo ejemplo pero debe funcionar para cualquier archivo que cumpla con estas condiciones.
#Ejemplo: alumnos.txt contiene
#1000;perez;juan;5;8
#3500;Garcia;Marcelo;2;5
#2400;pato;Miriam Alejandra;2;2
#
#En este caso se deben crear el archivo:
#condicion.txt conteniendo
#1000;perez;juan;5;8;FINAL
#3500;Garcia;Marcelo;2;5;PRIMERO
#2400;pato;Miriam Alejandra;2;2;AMBOS

def seleccionarEstadoDeAprobacion(datos, estados):
    notaAprobacion = 4

    #Obtenemos las notas
    nota1 = float(datos[3])
    nota2 = float(datos[4])

    if(nota1 < notaAprobacion and nota2 < notaAprobacion):
        datos.append(estados[2])
    elif(nota1 < notaAprobacion and nota2 > notaAprobacion):
        datos.append(estados[0])
    elif(nota1 > notaAprobacion and nota2 < notaAprobacion):
        datos.append(estados[1])
    else:
        datos.append(estados[3])

def nombreApellidoMayusculas(datos):
    nombre = datos[1]
    apellido = datos[2]

    nombres = nombre.split()
    apellidos = apellido.split()

    nombres = [nombre.capitalize() for nombre in nombres]
    apellidos = [apellido.capitalize() for apellido in apellidos]

    datos[1] = ' '.join(nombres)
    datos[2] = ' '.join(apellidos)

def main():
    try:
        alumnos = open('alumnos.txt')
        condiciones = open('condicion.txt', 'w')
    except IOError:
        print('Error')
    else:
        estados = ('PRIMERO', 'SEGUNDO', 'AMBOS', 'FINAL')

        for registro in alumnos:
            registro = registro.rstrip('\n')

            datos = registro.split(';')

            seleccionarEstadoDeAprobacion(datos, estados)
            nombreApellidoMayusculas(datos)

            condiciones.write(';'.join(datos) + '\n')

        alumnos.close()
        condiciones.close()

main()