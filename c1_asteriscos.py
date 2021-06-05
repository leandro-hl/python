def AsteriscosFijo(lineas):
    for i in range(lineas):
        for j in range(10):
            # le sacamos el salto de linea por un c vacio
            print("*", end="")
        # print vacio para hacer salto de linea
        print()

def main():
    lineas = int(input("Ingrese lineas: "))
    
    AsteriscosFijo(lineas)
    
main()