#Quitar los espacios de más entre palabras, dejando solo un espacio
cadena="#Me    encanta    Programar#"
print(cadena)
lista=cadena.split()
print(lista)
cadena = " ".join(lista)
print(cadena)

print()

#Si necesito analizar las palabras pero no perder los espacios originales
cadena="#Me    encanta    Programar#"
print(cadena)
lista=cadena.split(" ")
print(lista)
cadena = " ".join(lista)
print(cadena)