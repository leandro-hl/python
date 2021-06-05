import math as m

def deBinarioADecimal(binario):
    if(len(binario) == 0):
        return 0

    elif(binario[0] == '1'):
        return 2**(len(binario)-1) + deBinarioADecimal(binario[1:])
        
    else:
        return deBinarioADecimal(binario[1:])

def main():
    binario = '100111'

    decimal = deBinarioADecimal(binario)

    print(decimal)
main()