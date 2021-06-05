import random as r
import math as m

# Sin guía  de  las  funciones  a  desarrollar,  decidiendo  la estrategia 
# y la modularización delcódigo.Utilizandotodo lo visto hasta ahora.
# Un productor de naranjas desea contabilizarsus cajones de naranjas 
# según el peso para  poder  cargar el camión de reparto. 
# La  empresa cuenta  conN camionesque puedentransportar hasta media tonelada. 
# En un cajón entran 100 naranjas con un  peso  entre  200  y  300  gramos  cada  una,  
# si  la  naranja  supera  o  es  menor  al rango del  peso  indicado,  se  clasificapara  
# procesar  como  jugo.  
# Necesita  un programa  paraingresar  la  cantidad  de  naranjas  producidas  y  
# le  informe  cuántos cajones se pueden llenar, cuántas naranjas son para jugo y 
# si hay algún sobrante de  naranjas  quedebe  considerar  para  el  siguiente  reparto. 
# Calculare  informar,además,cuantos cajonesdeberáncargarsecamión, 
# para que todos queden con la misma  cantidad  de  cajones,  y  cuantos  
# cajonesquedaran  sin  cargar  en ningúncamión.
# Simular  el  peso  de cadanaranja  con un  número  al  azar  entre  150  y  350gramos.

#Funciones
def ObtenerNaranjasProducidas():
    cantidad = int(input("Ingrese la cantidad de naranjas producidas"))
    minimoPesoNaranja = 150
    maximoPesoNaranja = 350

    return [r.randint(minimoPesoNaranja, maximoPesoNaranja) for i in range(cantidad)]

def NaranjaEsParaJugo(peso):
    return peso < 200 or peso > 300

def SepararNaranjasParaJugo(naranjasParaEnviar, naranjasParaJugo):
    i = 0
    naranjasAEvaluar = len(naranjasParaEnviar) 
    while i < naranjasAEvaluar:
        naranja = naranjasParaEnviar[i]

        if(NaranjaEsParaJugo(naranja)):
            naranjasParaJugo.append(naranja)
            naranjasParaEnviar.remove(naranja)
            naranjasAEvaluar -= 1
            i -= 1

        i += 1

def CargarCajones(naranjasParaEnviar):
    naranjasPorCajon = 100

    cantidadNaranjasParaEnviar = len(naranjasParaEnviar)

    cantidadCajonesACargar = 0

    if(cantidadNaranjasParaEnviar < naranjasPorCajon):
        print("La cantidad de naranjas producidas no es suficiente para cargar un cajon")
        return cantidadCajonesACargar, cantidadNaranjasParaEnviar

    naranjasSobrantes = cantidadNaranjasParaEnviar % naranjasPorCajon

    cantidadCajonesACargar = m.floor(cantidadNaranjasParaEnviar / naranjasPorCajon)

    cajonesACargar = [0 for i in range(cantidadCajonesACargar)]

    cajonACargar = 0
    naranjasCargadas = 0
    while cajonACargar < len(cajonesACargar):
        naranja = naranjasParaEnviar.pop()

        cajonesACargar[cajonACargar] += naranja

        naranjasCargadas += 1

        if(naranjasCargadas == naranjasPorCajon):
            naranjasCargadas = 0
            cajonACargar += 1

    return cajonesACargar, naranjasSobrantes

def CargarCamiones(cajonesACargar):
    maximoPesoTransportePorCamion = 500000

    totalPesoATransportar = sum(cajonesACargar)

    cantidadCamionesNecesarios = m.ceil(totalPesoATransportar / maximoPesoTransportePorCamion)

    cantidadCajonesACargar = len(cajonesACargar)

    cajonesPorCamion = m.floor(cantidadCajonesACargar / cantidadCamionesNecesarios)

    cajonesSobrantes = cantidadCajonesACargar % cantidadCamionesNecesarios

    return cantidadCamionesNecesarios, cajonesPorCamion, cajonesSobrantes

#Programa Principal
def Main():
    naranjasProducidas = ObtenerNaranjasProducidas()

    naranjasParaEnviar = naranjasProducidas.copy()
    naranjasParaJugo = []

    SepararNaranjasParaJugo(naranjasParaEnviar, naranjasParaJugo)

    print("Naranjas producidas: ", naranjasProducidas)
    print("Naranjas para enviar: ", naranjasParaEnviar)
    print("Naranjas para jugo: ", naranjasParaJugo)

    cajonesACargar, naranjasSobrantes = CargarCajones(naranjasParaEnviar)

    print("Cajones para enviar: ", cajonesACargar)
    print("Naranjas sobrantes: ", naranjasSobrantes)

    camionesCargados, cajonesPorCamion, cajonesSobrantes = CargarCamiones(cajonesACargar)

    print("Camiones cargados: ", camionesCargados)
    print("Cajones por camion: ", cajonesPorCamion)
    print("Cajones sobrantes: ", cajonesSobrantes)
Main()