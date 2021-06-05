def MatrizEjeContador():



def matrizEjeComprension(n):
    return [[x//2+1 + y*n//2 if (x+y) % 2 == 1 else 0 for x in range(n)] for y in range(n)]