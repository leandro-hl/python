#Comparar caracteres: ejemplo:contar cuantos # tiene la cadena

cadena="#Me encanta Programar#"
print(cadena)
print()
print("utilizando método count:")
print("La cadena tiene",cadena.count("#"),"numerales")

cont=0
print("Recorrer Caracter a caracter utilizando índices:")
for i in range(len(cadena)):
    if cadena[i]=="#":
        print("Tiene un numeral en el índice",i)
        cont += 1
print("La cadena tiene",cont,"numerales")

print()       
cont=0
print("Recorrer caracter a caracter utilizando operador in:")
for caracter in cadena:
    if caracter=="#":
        print("Tiene un numeral en el índice",cont)
        cont += 1
print("La cadena tiene",cont,"numerales")

print()
cont=0
print("Recorrer caracter a caracter utilizando enumerate:")
for i,caracter in enumerate(cadena):
    if caracter=="#":
        print("Tiene un numeral en el índice",i)
        cont += 1
print("La cadena tiene",cont,"numerales")


print()
#utilizando método find
cont=0
pos=0
while pos!= -1:
    pos = cadena.find("#", pos)
    if pos !=-1:
        print("El numeral se encuentra en la posicion",pos)
        pos +=1 #muevo un lugar para que pueda buscar el siguiente numeral.
        cont +=1
print("La cadena tiene",cont,"numerales")