#Analizar cadenas que tienen significado, ejemplo una direccion de mail:
cadena="vgalati@uade.edu.ar"

#separar en partes para analizar:
lista=cadena.split("@")
print(lista)
lista=[lista[0]] + lista[1].split(".")
print(lista)