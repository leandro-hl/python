cadena="Me encanta Programar hoy 22 de mayo"
print(cadena)
#Recorrer una cadena:
# print("Recorrer Caracter a caracter utilizando índices:")
# for i in range(len(cadena)):
#     print(f"índice {i} letra {cadena[i]}")

# print("Recorrer caracter a caracter utilizando operador in:")
# for caracter in cadena:
#     print(caracter)
# 
# print("Recorrer caracter a caracter utilizando enumerate:")
# ncad=''
for i,caracter in enumerate(cadena):
    print(f"índice {i} letra {caracter}")
    ncad += caracter.lower()
ncad = cadena.lower()
print("La nueva cadena es:",ncad)    
#Con ciclo while 
# i=0
# while i < len(cadena):
#     print(f"índice {i} letra {cadena[i]}")
#     i += 1
