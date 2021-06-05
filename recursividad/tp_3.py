def sumar(n):
    if(n == 0):
        return 0

    return n + sumar(n-1)

def main():
    n = 4

    suma = sumar(n)

    print(suma)
main()