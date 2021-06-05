# A aprtir del archivo ventasEmpleados.csv:
# Buscar el empleado que vendio por mayor monto total
# Generar un nuevo archivo, donde se guarden todos los
# empleados y el monto total de ventas usando el formato de registros
# donde se indica el largo de cada campo antes del mismo
# Por ejemplo, el empleado 12345 con ventas de 100 se guarda:
# 051234503100
ruta = "2_parcial\\5_29_5_Recursividad\\"

def guardarTotalVentas(listaEmpleados, listaVentas):
    if len(listaEmpleados) != len(listaVentas) or len(listaEmpleados) == 0:
        raise IndexError("Las listas deben tener la misma cantidad de elementos y no estar vacias")
    
    try:
        archDestino = open(f"{ruta}ventasEmpleados.dat", "w")
    except IOError as msg:
        print(f"Error de entrada/salida: {msg}")
    else:
        for i in range(len(listaEmpleados)):
            empleado = str(listaEmpleados[i])
            total = str(listaVentas[i])
            registro = f"{len(empleado):02d}{empleado}"
            registro += f"{len(total):02d}{total}"
            archDestino.write(registro + "\n")
        archDestino.close()

def mostrarEmpleadoConMasVentas(listaEmpleados, listaVentas):
    """ Muestra el empleado con mas ventas y el total de ventas.
    Si las listas tienen distinto tamaño o estan vacias genera un IndexError
    """
    
    if len(listaEmpleados) != len(listaVentas) or len(listaEmpleados) == 0:
        raise IndexError("Las listas deben tener la misma cantidad de elementos y no estar vacias")
    
    maximo = max(listaVentas)
    print(f"El empleado que más vendió fue: {listaEmpleados[listaVentas.index(maximo)]:000006d}")
    print(f"Con un total de ventas de: $ {maximo}")

def cargarVentas():
    listaEmpleados = []
    listaTotales = []
    try:
        archOrigen = open(f"{ruta}ventasEmpleados.csv")
    except IOError as msg:
        print(f"Error de entrada/salida: {msg}")
    else:
        for reg in archOrigen:
            reg = reg.replace("\n","")
            lstReg = reg.split(";")
            try:
                nroEmp = int(lstReg[0])
                total = int(lstReg[1])
            except ValueError:
                print(f"No pudo convertirse a numero registro: {reg}")
            except IndexError:
                print(f"No pudo dividirse el registro: {reg}")
            else:
                if nroEmp in listaEmpleados:
                    listaTotales[listaEmpleados.index(nroEmp)] += total
                else:
                    listaEmpleados.append(nroEmp)
                    listaTotales.append(total)
        archOrigen.close()
    return listaEmpleados, listaTotales 

def main():
    lstEmpleados, lstVentas = cargarVentas()
    try:
        guardarTotalVentas(lstEmpleados, lstVentas)
    except IndexError as msg:
        print(f"Ocurrio un error al guardar las ventas: {msg}")

    try:
        mostrarEmpleadoConMasVentas(lstEmpleados, lstVentas)
    except IndexError as msg:
        print(f"Ocurrio un error al buscar el mejor vendedor: {msg}")
        
    
if __name__ == "__main__":
    main()