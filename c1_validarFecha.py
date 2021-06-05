# Funciones
def IngresarPositivo():
    numero = int(input("Ingrese un numero positivo: "))
    
    while numero < 1:
        print("El numero ingresado no es positivo")
        
        numero = int(input("Ingrese un numero positivo: "))
        
    return numero

def EsBisiesto(anio):
    anioBisiesto = True
    
    if (anio % 4 == 0):
        if (anio % 100 == 0) and (anio % 400 != 0):
            anioBisiesto = False
    else:
        anioBisiesto = False
        
    return anioBisiesto
    
def ValidarFecha(dia, mes, anio):
    # Supongo que la fecha es valida
    fechaValida = True
    
    if dia < 1 or mes < 1 or anio < 1:
        # Algun valor es negativo
        fechaValida = False
    elif (mes > 12):
        # Mes es mayor a 12
        fechaValida = False
    elif (dia > 31):
        # Dia es mayor a 31
        fechaValida = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        # Mes de 30 dias y dia mayor a 30
        fechaValida = False
    elif (mes == 2) and EsBisiesto(anio) and dia > 29:
        # Anio bisiesto y el dia de febrero mayor a 29
        fechaValida = False
    elif (mes == 2) and not EsBisiesto(anio) and dia > 28:
        # febrero mayor a 28
        fechaValida = False
        
    return fechaValida

def main():
    dia = IngresarPositivo()
    mes = IngresarPositivo()
    anio = IngresarPositivo()
    
    fechaValida = ValidarFecha(dia, mes, anio)
    
    if(fechaValida):
        print("Todo bien!")
    else:
        print("Todo bien!")

# Programa principal
main()