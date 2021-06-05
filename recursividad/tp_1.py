def contarUnidades(numero):
    if(numero < 1):
        return 0
    else:
        return 1 + contarUnidades(numero/10)

def main():
    numero = 1390

    resultado = contarUnidades(numero)
    #expected: 4
    print(resultado)
main()