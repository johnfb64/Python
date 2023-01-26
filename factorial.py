############################################################################
# Codigo por John Fernando Ballén - 25-01-2022                             # 
# Codigo que calcula un factorial.                                         #
# El programa esta realizado con paradigma POO, tiene getters y setters    #
############################################################################



##### Clase que calcula factorial ###############################################
class Factorial:
    def __init__(self,numero):
        self._numero = numero
        acum = 1
        for i in range(1, numero+1):
            acum = i * acum            
            
        print ("Factorial de " + str(numero) + "!: " + str(acum))  
        
    #Getter y setter
    @property
    def numero(self):
        return self._numero
        
    @numero.setter
    def numero(self,numero):
        self._numero = numero
####################################################################################        
    
##### OBJETO #######################################################################
       

print("Este es el programa de factoriales")
num = int(input("Ingresa un numero: "))
factorial1 = Factorial(num)

if num > 0:
    print(factorial1.numero)
else:
    print("Numero igual o menor a 0, por favor ingrese un numero valido")

####################################################################################