import matrices_tools as tool

def Main():
    matriz = tool.CrearCeroMatrizConArea()

    i = 0
    j = 0
    maximo = 0
    minimo = 0
    items = 1
    largo = len(matriz)
    tope = largo - 1    
    numero = 1
    fin = False

    deArribaHaciaAbajo = False

    while(not fin):
        if(maximo == minimo and maximo == tope and items == 1):
            fin = True

        for k in range(items):
            matriz[i][j] = numero
            numero += 1

            if(deArribaHaciaAbajo):
                if(j > minimo):
                    j -= 1

                if(i < maximo):
                    i += 1

            else:
                if(i > minimo):
                    i -= 1

                if(j < maximo):
                    j += 1

        if(maximo == tope and minimo < tope):
            minimo += 1
            items -= 1

        if(maximo < tope):
            maximo += 1
            items += 1

        deArribaHaciaAbajo = not deArribaHaciaAbajo

        if(deArribaHaciaAbajo):
            i = minimo
            j = maximo
        else:
            j = minimo
            i = maximo

    print(matriz)
Main()