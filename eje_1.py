import re
class email:
    __IdCuenta=''
    __dominio=''
    __Tipodom=''
    __contra=''

    def __init__(self,id,dom,Tipodom,contra):
        
        self.__IdCuenta=id
        self.__dominio=dom
        self.__Tipodom=Tipodom
        self.__contra=contra

    def Retornaemail(self):
        return self.__IdCuenta+ "@" +self.__dominio+"."+self.__Tipodom

    def getdom(self):
        return print(self.__dominio)

    def crearCuenta(self,correo,contra):
        grupo=re.search(r'([a-zA-Z0-9./-_]+)@([a-zA-Z0-9./-]+)\.([a-z]+)',correo)
        if(type(grupo) == re.Match):
            self.__init__(grupo.group(1),grupo.group(2),grupo.group(3),contra)
            print("Cuenta creada exitosamente")
        else: print("Usted no ingreso un correo valido.\n")
    
    def cambioc(self):
        return self.__contra

    def changepass(self,new):
        self.__contra=new
        return self.__contra

    def testing(self):
        c1="informatica.fcefn@gmail.com"
        c1p="555hola"
        c2="wicc2019@unsj-cuim.edu"
        c2p="876tt"
        c3="error@gmail,com"
        c3p=63344
        self.crearCuenta(c1,c1p)
        self.crearCuenta(c2,c2p)
        self.crearCuenta(c3,c3p)
        