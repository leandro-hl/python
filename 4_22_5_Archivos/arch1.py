try:
    arch=open("zen.txt")
except IOError:
    print("No se logro abrir el archivo")
else:
    #Procesar los datos del archivo.
    for registro in arch:
        #Quito el caracter \n
        registro=registro.replace("\n","")
        lista=registro.split(" ")
        print(lista)
        print(registro)    
    arch.close()