from eje_1 import email
import csv
if __name__ == '__main__':
    
    nom=input("Ingrese su nombre: ")
    id=input("Ingrese su id: ")
    dom=input("Ingrese el dominio ")
    tipodom=input("Ingrese el tipo de dominio: ")
    contra=input("Ingrese su contraseña actual: ")
    mail=email(id,dom,tipodom,contra)
    print("Estimado {} te enviaremos tus mensajes a la direccion".format(nom),mail.Retornaemail())


    print("---------Cambio de Contraseña----------")
    contra=input("Para cambiar su contraseña: \n Ingrese la contraseña actual: ")
    while contra != mail.cambioc():
        contra=input("Contraseña Incorrecta vuelva a ingresarla.")
    else: 
        new=input("Ingrese la nueva contraseña: ")
        mail.changepass(new)  
        print("La contraseña ha sido cambiada con exito")

    print("--------Crear Cuenta-----------")
    mail2=email('','','','')
    correo=input("Ingrese un correo electronico para crear una cuenta: ")
    contra=input("Ingrese su contraseña : ")
    mail2.crearCuenta(correo,contra)
    

    print("---------Busca Dominio----------")
    archivo=open('gmail.txt')
    reader=csv.reader(archivo,delimiter=',') 


    domi=input("Ingrese un Dominio: ")
    conta=0
    for fila in reader:
        if fila[1] == domi:
            conta+=1

    print("Para el Dominio {} la cantidad de usuarios es {}".format(domi,conta))
    print("-------Testing-------")
    mail3=email("","","","")
    mail3.testing()

    