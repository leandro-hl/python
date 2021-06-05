#lista=[12,23,30,40]
lista=["Hola","Mundo"]
print(lista)
#recorrer con los indices
for i in range(len(lista)):
    print(f"el elemento {lista[i]} esta en posicion {i}")
       
print()    
#recorrer por los elementos
for cadena in lista:
    print(f"El elemento es: {cadena}")
    
    
print()
for i,elemento in enumerate(lista):
    print(f"el elemento {elemento} esta en posicion {i}")

i=0
while i <= len(lista)//2:
   print(f"el elemento {lista[i]} esta en posicion {i}")
   i += 1