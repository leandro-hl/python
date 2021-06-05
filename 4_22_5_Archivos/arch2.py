try:
    arch=open("zen.txt")
    archN=open("Nuevozen.txt","w")
except IOError:
    print("No se logro abrir el archivo")
else:
    #Procesar los datos del archivo.
    cadena = arch.readline()  #UNA LINEA! o sea un registro
    while cadena!='':
        #Quito el caracter \n
        cadena=cadena.replace("\n","")
        cadena=cadena.lower()
        archN.write(cadena+"\n") #un registro.

        cadena = arch.readline()  #UNA LINEA!
    arch.close()
    archN.close()
    print("Archivo creado")