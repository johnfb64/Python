import os

class Cuenta:
    #Constructor
    def __init__(self,titular,monto,saldo):
        self._titular = titular
        self._monto = monto
        self._saldo = saldo
    
    #Declaración de setters y getters
    #Setter y getter del titular
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self,titular):
        self._titular = titular
    #Setter y getter de monto
    @property
    def monto(self):
        return self._monto
    
    @monto.setter
    def monto(self,monto):
        self._monto = monto
    #Setter y getter de saldo
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,saldo):
        self._saldo = saldo

    #Meotodo para ingresar monto, identifica titular, indica valor ingresado por el usuario y suma monto a saldo y guarda. 
    def ingresar(self):                    
        print ("Titular de la cuenta identificado como: " + self.titular)        
        print ("El valor agregado es de: " + str(self.monto))
        self.saldo += self.monto
        print ("Tiene un saldo actual de : " + str(self.saldo))
        
    #Meotodo para retirar monto, identifica titular, indica valor ingresado por el usuario y suma monto a saldo y guarda.             
    def retirar(self):
        print ("Titular de la cuenta identificado como: " + self.titular)
        print ("Retiro de monto por: " + str(self.monto))
        #Si el saldo es mayor que el monto a retirar, permitira a hacer la operación
        if self.saldo > self.monto:
            self.saldo -= self.monto
            print ("El valor de su saldo actual es: " + str(self.saldo))
        else:
            print ("Saldo insuficiente, agregue saldo por opcion 1...")           
    #Meotodo para mostrar el saldo.     
    def mostrar(self):
        print ("El titular de la cuenta identificado como: " + self.titular)
        print ("El saldo de la cuenta actualmente es de: " + str(self.saldo))
        
#Inicia la logica del programa
print ("########### PROGRAMA CUENTA BANCARIA DE USUARIO ########################")
#Estas variables se inicalizan en 0.
saldo = 0
monto = 0
#Antes del bucle, pide nombre de titular. 
titular = str(input("Ingrese nombre del titular: "))
operacion1 = Cuenta(titular,monto,saldo)
while True:
    os.system('cls')
    #Menu de operación.
    menu = int(input("1. Ingresar monto. \n2. Retirar monto. \n3. consultar saldo. \n0. salir. \nSeleccione una Opción: "))
    if menu == 0:
        break
    else:        
        #Opcion de añadir fondos. 
        if menu == 1:
            os.system('cls') 
            print ("##### MODULO PARA INGRESAR MONTO ########")                       
            #Aqui hay que tener en cuenta que para retener variables se debe guardar el valor en la instancia (operacion1.monto)
            #Si no se hace de esta manera, cada vez que el bucle se ejecute va a sobreescribir la data. 
            operacion1.monto = int(input("Ingrese el monto a ingresar: "))                      
            operacion1.ingresar()
            print("")
            input("Presione Enter para continuar...")
            
        #Opcion de retirar fondos. 
        elif menu == 2:
            os.system('cls')
            print ("##### MODULO PARA RETIRAR MONTO ########")
            operacion1.monto = int(input("Ingrese el monto a retirar: "))
            operacion1.retirar()
            print("")
            input("Presione Enter para continuar...")
            
        #Opción de visualizar fondos       
        elif menu == 3:
            os.system('cls')
            print ("######## MODULO PARA RETIRAR MONTO ########")
            print (operacion1.mostrar())
            print("")
            input("Presione Enter para continuar...")
            
        #opción default de seleccion no valida.     
        else:            
            print ("Seleccione una opcion valida")
        
