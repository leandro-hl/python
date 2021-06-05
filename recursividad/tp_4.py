def multiplicar(x, y):
    if(y == 0):
        return 0

    return x + multiplicar(x, y-1)

def main():
    x = 4
    y = 5

    suma = multiplicar(x, y)

    print(suma)
main()