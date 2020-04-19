import csv
from Ejercicio2 import ViajeroFrecuente
import re
class manejador:
    __lista=[]
    def crearlista(self):
        archivo=open("archivo.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            num=int(fila[0])
            dni=re.match('^[0-9]+$',fila[1])
            nom=str(fila[2])
            ap=str(fila[3])
            millaacu=float(fila[4])
            if type(num)==int and type(dni)==re.Match and type(nom)==str and type(ap)== str and type(millaacu)==float:
                viajero=ViajeroFrecuente(num,dni,nom,ap,millaacu)
                self.__lista.append(viajero)
        return(self.__lista)
  