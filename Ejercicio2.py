
import re
class ViajeroFrecuente:
    __num= ''
    __DNI= ''
    __nombre= ''
    __apellido= ''
    __millaacu= 0.0

    def __init__(self,num,dni,nom,apellido,millaacu):
            self.__num=num
            self.__DNI=dni
            self.__nombre=nom
            self.__apellido=apellido
            self.__millaacu=millaacu 
    def cantidaddemillas(self):
        return self.__millaacu

    def acumularMillas(self,cant):
        self.__millaacu+=cant
        return self.__millaacu
    def canjearMillas(self,cant):
        if cant <= self.__millaacu:
            self.__millaacu-=cant
            print("Millas canjeadas\n")
        else: print("ERROR, la cantidad ingresada supera la cantidad que usted posee.\n")

    