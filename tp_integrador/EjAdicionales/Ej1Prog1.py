# Programa 1: Crear una lista con N elementos al azar entre 1 y 100.
# Mostrar el promedio y aquellos elementos que sean mayores al promedio,
# ordenados de menor a mayor. (utilizar la funcion sum y el método count (?).
# Crear la lista por comprensión (o con filter?) de los elementos que superan el promedio)
import FnGenLst

def main():
    cant = int(input("Cantidad de elementos: "))
    while cant < 0:
        print("La cantidad no puede ser negativa")
        cant = int(input("Cantidad de elementos: "))
    lista = FnGenLst.generarLista(cant)
    promLista = sum(lista) / cant
    print(f"La lista completa es: {lista}")
    print(f"El promedio es {promLista:5.2f}")
    listaMayoresComprension = [x for x in lista if x > promLista]
    listaMayoresComprension.sort()
    print(f"La lista por comprensión es: {listaMayoresComprension}")
    listaMayoresFilter = list(filter(lambda x : x > promLista, lista))
    listaMayoresFilter.sort()
    print(f"La lista por comprensión es: {listaMayoresFilter}")
    
if __name__ == "__main__": 
    main()