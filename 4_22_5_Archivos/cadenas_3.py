#Separar en palabras cuando se necesita analizar cada una de las palabras.

cadena="#Me encanta Programar#"
print(cadena)

print("Separar en palabras sin indicar separador")
lista=cadena.split()
print(lista)
print("crear una cadena de una lista:")
cad = " ".join(lista)
print(cad)

print()
print("Separar en palabras indicando separador espacio")
lista=cadena.split(" ")
print(lista)

print("crear una cadena de una lista:")
cad = " ".join(lista)
print(cad)