import random as r
import HerenuLeandro_ModuloInformes as tools

def crearHistorialVentas():
    obtenerNumeroAzar = lambda desde, hasta : r.randint(desde-1, hasta-1)

    meses = 12
    productos = 12
    maximoUnidades = 2000
    ventasDisponiblesPorProducto = [maximoUnidades for i in range(productos)]

    historicoVentas = [[0 for j in range(productos)] for i in range(meses)]

    # Mientras tengamos algun producto en stock, cargamos la venta
    while sum(ventasDisponiblesPorProducto) > 0:
        
        productoVendido = obtenerNumeroAzar(1, productos)

        ventasDisponibles = ventasDisponiblesPorProducto[productoVendido]

        if(ventasDisponibles > 0):
            mesVendido = obtenerNumeroAzar(1, meses)

            cantidadVendida = r.randint(0, ventasDisponibles)

            historicoVentas[mesVendido][productoVendido] += cantidadVendida

            ventasDisponiblesPorProducto[productoVendido] -= cantidadVendida

    return historicoVentas

def generarTotalesPorSemestre(historialVentas):
    totalesVendidosPrimerSemestre = tools.calcularVentasTotales(historialVentas, 1, 6)
    totalesVendidosSegundoSemestre = tools.calcularVentasTotales(historialVentas, 7, 12)

    return totalesVendidosPrimerSemestre, totalesVendidosSegundoSemestre

def generarInformeCrecimientoVentas(totalesVendidosPrimerSemestre, totalesVendidosSegundoSemestre):
    ventasPrimerSemestreDecrecen = tools.ventasDecrecen(totalesVendidosPrimerSemestre)

    if(ventasPrimerSemestreDecrecen):
        print("Las ventas en el primer semestre del año pasado decrecieron")
    else:
        print("Las ventas en el primer semestre del año pasado crecieron")

    ventasSegundoSemestreCrecen = tools.ventasCrecen(totalesVendidosSegundoSemestre)

    if(ventasSegundoSemestreCrecen):
        print("Las ventas en el segundo semestre del año pasado crecieron")
    else:
        print("Las ventas en el segundo semestre del año pasado decrecieron")

def generarInformeMesMayorVentas(historialVentas, totalesAnualizados):
    mesConMayorCantidadVentas = tools.obtenerMesConMayorCantidadVentas(totalesAnualizados)

    mesesDelAnio = tools.obtenerMesesDelAnio()

    print("El mes con mayor cantidad de ventas fue: ", mesesDelAnio[mesConMayorCantidadVentas])

    ventasMes = historialVentas[mesConMayorCantidadVentas]

    productoMenosVendidoDelMes = ventasMes.index(min(ventasMes))

    descripcionProductos = tools.obtenerProductos()

    print("El producto menos vendido del mes fue: ", descripcionProductos[productoMenosVendidoDelMes])

def Main():
    historialVentas = crearHistorialVentas()

    print(historialVentas)

    totalesVendidosPrimerSemestre, totalesVendidosSegundoSemestre = generarTotalesPorSemestre(historialVentas)

    generarInformeCrecimientoVentas(totalesVendidosPrimerSemestre, totalesVendidosSegundoSemestre)

    totalesAnualizados = totalesVendidosPrimerSemestre + totalesVendidosSegundoSemestre

    generarInformeMesMayorVentas(historialVentas, totalesAnualizados)
Main()