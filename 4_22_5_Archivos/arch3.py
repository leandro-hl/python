try:
    arch=open("empleados.txt")
    #Procesar los datos del archivo.
    cadena = arch.readline()  #UNA LINEA! o sea un registro
    while cadena!='':
        #Quito el caracter \n
        cadena=cadena.replace("\n","")
        print(cadena)
        cadena = arch.readline()  #UNA LINEA!

except IOError:
    print("No se logro abrir el archivo")
    
finally:
    try:
        arch.close()
    except:
        pass