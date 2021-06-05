# Programa 2: Crear una lista al azar, luego informar para cada valor, cuántas veces se repite.
# El informe No debe repetir el número. (Aca si se debe usar count)
import FnGenLst

def main():
    lista = FnGenLst.generarLista(20, 1, 10)
    listaInformados = []
    for x in lista:
        if x not in listaInformados:
            print(f"El elemento {x} se repite {lista.count(x)} veces.")
            listaInformados.append(x)
            
if __name__ == "__main__": 
    main()