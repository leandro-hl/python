def obtenerMesesDelAnio():
    return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def obtenerProductos():
    return ["Zapatillas", "Lentes", "Ojotas", "Buzo con cierre", "Corbata", "Medias", "Zapatos", "Campera", "Sandalia", "Buzo", "Jean", "Remera"]

def calcularVentasTotales(historialVentas, desdeMes=1, hastaMes=6):
    """ 
        realiza una agregacion de las ventas por mes.
        Parametros: 
        historialVentas: matriz. Cada fila un mes, cada columna una cantidad vendida por producto. Obligatorio. 
        desdeMes: mes desde el cual se desea obtener las ventas. Default:1 (Enero).
        hastaMes: mes hasta el cual se desea obtener las ventas. Default:6 (Junio).
    """
    return [sum(ventas) for ventas in historialVentas[desdeMes-1: hastaMes]]

def ventasDecrecen(ventas):
    return ventas[0] > ventas[-1]

def ventasCrecen(ventas):
    return ventas[0] < ventas[-1]

def obtenerMesConMayorCantidadVentas(ventas):
    return ventas.index(max(ventas))