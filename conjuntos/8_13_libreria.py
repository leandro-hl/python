#Una librería almacena su lista de precios en un diccionario. Diseñar un programa
#para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
#listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
#costoso que venden en el comercio.

def main():
    precios = { 'cuadernos': 15.5, 'lapiz': 5, 'tele': 200 }

    precios['cuadernos'] += precios['cuadernos'] * 0.15

    mayorPrecio = max(precios.values())
    
    for item, precio in precios.items():
        if precio == mayorPrecio:
            itemMasCaro = item
            break

    print(f'El item mas caro es: { itemMasCaro } con un valor de { mayorPrecio }')
main()