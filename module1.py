from Ejercicio2 import ViajeroFrecuente 
from module2 import manejador

def op0(i):
        print("--Salir--\n")
def op1(i):
        print("---Consulta Millas---\n")
        print(lista[i].cantidaddemillas())
        
def op2(i):
        print("---Acumular Millas---\n")
        mil=float(input("Ingrese la cantidad de millas a acumular: "))
        print(lista[i].acumularMillas(mil))
def op3(i):
        print("---Canjear Millas---\n")
        mil=float(input("Ingrese la cantidad de millas a canjear: \n"))
        lista[i].canjearMillas(mil)

switcher= {
    0:op0,
    1:op1,
    2:op2,  
    3:op3      
    }
def switch(op,i):
    func = switcher.get(op, lambda: print("Opción incorrecta"))
    func(i)
    


if __name__ == '__main__':
    l=manejador()
    lista=l.crearlista()

    i=int(input("Ingrese el numero del viajero: \n"))
    
    while i<=0 or i>20:
        i=int(input("Usted no ingreso un numero valido, vuelva a intentarlo: "))   
    else:
        i-=1
    bandera=False
    while not bandera:
        print("---------------MENU-------------")
        print("-----------------------------------")
        print("1.Consultar cantidad de millas. \n")
        print("2.Acumular millas. \n")
        print("3.Canjear millas. \n")
        op=int(input("Seleccione una Opcion (0 para salir)\n"))
        switch(op,i)
        bandera = int(op)==0
    