import csv
from clase7 import ViajeroFrecuente

def listadeviajeros():
    listaViajeros=[]    
    with open('datos.csv','r')as archivo:
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
            listaViajeros.append(viajero)  
    return(listaViajeros) 
