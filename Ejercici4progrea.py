import random
import math

class Cuenta:
    def __init__(self, ID, nombre, fecha_apertura, numero_cuenta, saldo,fecha_vencimiento):
        self.ID = ID
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.fecha_vencimiento=fecha_vencimiento

    def retirardinero(self,restadinero):
        if(restadinero>self.saldo):
            print("Error, no hay suficiente dinero en la cuenta")
        else:
            self.saldo = self.saldo -restadinero
            print("retirar dinero se ha completado")

    def ingresardinero(self,ingresadinero):
        self.saldo=self.saldo+ingresadinero
        print("dinero ingresado se ha completado")
        

    def transferirdinero(self,transfieredinero,nombreobjetotransferir): 
        if(transfieredinero>self.saldo):
            print("Error, no hay suficiente dinero en la cuenta")
        else:
            self.saldo = self.saldo -transfieredinero
            nombreobjetotransferir.saldo = nombreobjetotransferir.saldo + transfieredinero
            print("transferir dinero se ha completado")

    

class Cuentaplazofijo:
    def __init__(self, ID, nombre, fecha_apertura, numero_cuenta, saldo,fechalimite,fecha_vencimiento):
        self.ID = ID
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.fechalimite = fechalimite
        self.fecha_vencimiento=fecha_vencimiento

    def retirardineroplazofijo(self, fecha_actual_dias,fecha_limite_dias,fecha_actual_años,fecha_limite_años,fecha_actual_meses,fecha_limite_meses, restadinero):
        #if(fechalimite>fechaactual):
        if(fecha_limite_años<=fecha_actual_años):
            if(fecha_limite_meses<=fecha_actual_meses):
                if(fecha_limite_dias<fecha_actual_dias):
                    self.saldo = self.saldo -restadinero
                    print("retirar dinero se ha completado")

        else:
            self.saldo = self.saldo -restadinero -(restadinero*0.05)
            print("retirar dinero se ha completado con una comision")

    def ingresardinero(self,ingresadinero):
        self.saldo=self.saldo+ingresadinero
        print("dinero ingresado se ha completado")

    def transferirdinero(self,transfieredinero,nombreobjetotransferir,fechalimite,fechaactual): 
        if(transfieredinero>self.saldo):
            print("Error, no hay suficiente dinero en la cuenta")
        else:
            if(fechalimite>fechaactual):
                self.saldo = self.saldo -transfieredinero
                nombreobjetotransferir.saldo = nombreobjetotransferir.saldo + transfieredinero
                print("transferir dinero se ha completado")  

            else:
                self.saldo = self.saldo -transfieredinero -(transfieredinero*0.05)
                nombreobjetotransferir.saldo = nombreobjetotransferir.saldo + transfieredinero
                print("transferir dinero se ha completado")            
             
    


class CuentaVIP:
    def __init__(self, ID, nombre, fecha_apertura, numero_cuenta, saldo, saldonegmax,fecha_vencimiento):
        self.ID = ID
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.saldonefmax = saldonegmax
        self.fecha_vencimiento=fecha_vencimiento

    def retirardinero(self,restadinero,saldonegmax):
        if(restadinero>(self.saldo+saldonegmax)):
            print("Error, no puede endeudarse tanto")
        else:
            self.saldo = self.saldo -restadinero
            print("retirar dinero se ha completado")

    def ingresardinero(self,ingresadinero):
        self.saldo=self.saldo+ingresadinero
        print("dinero ingresado se ha completado")

    def transferirdinero(self,transfieredinero,nombreobjetotransferir,saldonegmax): 
        if(transfieredinero>(self.saldo+saldonegmax)):
            print("Error, no puede endeudarse tanto")
        else:
            self.saldo = self.saldo -transfieredinero
            nombreobjetotransferir.saldo = nombreobjetotransferir.saldo + transfieredinero
            print("transferir dinero se ha completado")


ID=1
nombre="paco" 
fecha_apertura_dias = 0
fecha_apertura_meses=0
fecha_apertura_años=0
fecha_vencimiento_dias =0
fecha_vencimiento_meses=0
fecha_vencimiento_años=0
while True:
    fecha_apertura_dias=random.randint(1,31)
    fecha_vencimiento_dias=random.randint(1,31)
    fecha_apertura_meses=random.randint(1,12)
    fecha_vencimiento_meses=random.randint(1,12)
    fecha_apertura_años=random.randint(1900,2022)
    fecha_vencimiento_años=random.randint(2022,2100)
    if(fecha_apertura_años<=fecha_vencimiento_años):
        if(fecha_apertura_meses<=fecha_vencimiento_meses):
            if(fecha_apertura_dias<fecha_vencimiento_dias):
                break

fecha_apertura = fecha_apertura_dias*1000000 +fecha_apertura_meses*10000 +fecha_apertura_años
fecha_vencimiento = fecha_vencimiento_dias*1000000 +fecha_vencimiento_meses*10000 +fecha_vencimiento_años


numero_cuenta = random.randint(0,999999999999) #no tengo ni idea d como comprobar q sea igual q los otros numeors d cuenta

saldo=10000
        
    

cuenta1= Cuenta(ID,nombre,fecha_apertura,numero_cuenta,saldo,fecha_vencimiento)
ID+=1

#si no quieres repetir esto para cada cuenta creada lo puedes meter en un while True: y preguntar por teclado si quiere seguir creando cuenta, pero nose como leer por teclado
nombre="juan" 
while True:
    fecha_apertura_dias=random.randint(1,31)
    fecha_vencimiento_dias=random.randint(1,31)
    fecha_apertura_meses=random.randint(1,12)
    fecha_vencimiento_meses=random.randint(1,12)
    fecha_apertura_años=random.randint(1900,2022)
    fecha_vencimiento_años=random.randint(2022,2100)
    if(fecha_apertura_años<=fecha_vencimiento_años):
        if(fecha_apertura_meses<=fecha_vencimiento_meses):
            if(fecha_apertura_dias<fecha_vencimiento_dias):
                break

fecha_apertura = fecha_apertura_dias*1000000 +fecha_apertura_meses*10000 +fecha_apertura_años
fecha_vencimiento = fecha_vencimiento_dias*1000000 +fecha_vencimiento_meses*10000 +fecha_vencimiento_años


numero_cuenta = random.randint(0,999999999999) 

saldo=10000
cuenta2= Cuenta(ID,nombre,fecha_apertura,numero_cuenta,saldo,fecha_vencimiento)
ID+=1

cuenta1.transferirdinero(2000,cuenta2)


cuenta2.transferirdinero(2000,cuenta1)

cuenta1.ingresardinero(575)
cuenta2.ingresardinero(575)

cuenta1.retirardinero(78)
cuenta2.retirardinero(78)

fecha_limite_dias=12
fecha_limite_meses=10
fecha_limite_años=2010
fecha_actual_dias=12
fecha_actual_meses=10
fecha_actual_años=1010

