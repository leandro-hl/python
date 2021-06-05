def main():
    dic = {
        'lala': 0,
        'po': 1,
        'pepe': 0
    }

    buscar = 0
    claves = [item[0] for item in filter(lambda tupla: tupla[1] == buscar, dic.items())]

    print(claves)

main()