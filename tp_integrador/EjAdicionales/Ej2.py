# Un productor de naranjas desea contabilizar sus cajones de naranjas según el peso
# para poder cargar el camión de reparto. La empresa cuenta con N camiones para
# transportar los cajones. En un cajón entran 100 naranjas con un peso
# entre 200 y 300 gramos cada una, si la naranja supera o es menor al rango del peso
# indicado, se clasifica para procesar como jugo. Necesita un programa para ingresar
# la cantidad de naranjas producidas y le informe cuántos cajones se pueden llenar,
# cuántas naranjas son para jugo y si hay algún sobrante de naranjas que debe considerar
# para el siguiete reparto. Calcular e informar, además, cuantos cajones deberan cargarse
# por camion, para que todos queden con la misma cantidad de cajones, y cuantos cajones
# quedaran sin cargar en ningun camion.
# Simular el peso de cada naranja con un número al azar entre 150 y 350

from random import randint as rndm

def main():
    cantCam = int(input("Ingrese la cantidad de camiones: "))
    cantNar = int(input("Ingrese la cantidad de naranjas: "))
    cantCajones = 0 # Cantidad de cajones llenos
    paraJugo = 0 # Cantidad de naranjas para jugo
    nar = 0 # Iterador de naranjas
    
    while nar < cantNar:
        narCajon = 0 #Iterador de naranjas en un cajon
        while narCajon < 100 and nar < cantNar:
            pesoNar = rndm(150, 350)
            if pesoNar >= 200 and pesoNar <= 300:
                narCajon += 1
            else:
                paraJugo += 1
            nar += 1
        if narCajon == 100:
            cantCajones += 1
    
    print(f"Se llenaron {cantCajones} cajones de naranjas, con un sobrante de {narCajon} naranjas y {paraJugo} naranjas fueron separadas para jugo.")
    print(f"Se deben cargar {cantCajones // cantCam} cajones por camión, y quedarán {cantCajones % cantCam} sin cargar en ningún camión.")

if __name__ == "__main__": 
    main()