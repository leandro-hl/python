import random as r 

# Intercalar los elementos de una lista entre los elementos de otra. La intercalación
# deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
# una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
# y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

def Intercalar(lista1, lista2):
    incrementador = 1
    for i, valor in enumerate(lista2):
        lista1[i+incrementador:i+incrementador] = [valor]
        incrementador+= 1
        

def Main():
    lista1 = [r.randint(1,50) for i in range(5)]
    lista2 = [r.randint(1,50) for i in range(5)]

    print(lista1)
    print(lista2)

    Intercalar(lista1, lista2)

    print(lista1)
Main()