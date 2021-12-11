"""
VARIABLES DE CLASE EN PYTHON
NOTAS:
- metodos estaticos: Se asocian directo a la clase. Para llamarlo se usa el decorador @staticmethod.

-------------------------------METODOS ESTATICOS---------------------------------------------------------------------
- Los metodos estaticos trabajan solo con la clase y no con los objetos. No reciben el parametro de self.
- Los metodos estaticos y las variables de instancia, se asocian con la clase.
- Las variables de instancia se crean solo cuando se define el objeto, por lo que los metodos estaticos no podran
  acceder a estas variables.
- Cuando se carga la clase en memoria, se pueden crear objetos. Despues de esto se le pueden asociar sus variables y
  metodos de instancia. ESTO ES CONTEXTO ESTATICO.
- Cuando se trabaja con los objetos una vez se carga la clase en memoria, es CONTEXTO DINAMICO.
- Un objeto puede acceder puede acceder al contexto estatico cuando la clase se haya cargado en memoria.


--------------------------------METODOS DE CLASE--------------------------------------------------------------------
- Para definir un metodo de clase se utiliza el decorador @classmethod
- Los metodos de clase, NO pueden a los atributos de una instancia, pero si pueden modificar los atributos de una clase.
- Los metodos estaticos NO aceptan como parametro ni la clase  ni la instancia. NO PUEDEN MODIFICAR EL ESTADO NI DE LA CLASE
  NI DE LA INSTANCIA
- Por lo tanto el uso de los métodos estáticos pueden resultar útil para indicar que un método no modificará el estado
  de la instancia ni de la clase


"""

class MiClase:
#Variable de clase: variable asociada a la clase
    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        #Variable de instancia: Se asocia solamente a las instancias de objetos que se crean.
        self.variable_instancia = variable_instancia


# Metodo estatico
    @staticmethod
    def metodo_estatico():
        #self.variable_instancia - Esta linea genera error por que al ser estatico no podria acceder a self.
        #En cambio se puede acceder a la variable clase de forma indirecta (con MiClase.....)
        MiClase.variables_clase
        #para utilizar este metodo se llamara llamando a la clase

#METODO DE CLASE
    @classmethod
        #El parametro cls se recibio de manera automatica. cls = class. Con este parametro se accede a las variables de
        # clase.
    def metodo_clase(cls):
        #Con cls se acceder a variables_clase
        print(cls.variables_clase)

    #Definiendo metodo de instancia
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        #El contexto dinamico puede acceder al contexto estatico
        print(self.variables_clase)
        print(self.variable_instancia)

#Se accede al metodo estatico
MiClase.metodo_estatico()


print('-'.center(50,'-'))


print(MiClase.variables_clase)
ObjEjemplo = MiClase('Valor variable instancia')
print(ObjEjemplo.variable_instancia)
ObjEjemplo2 = MiClase('Otro valor variable de instancia')
print(ObjEjemplo2.variable_instancia)

#Esta linea define variable de clase de forma rapida
MiClase.variable_clase2 = 'variable de clase realizada de forma rapida'
#Se puede acceder desde la clase avariable_Clase2
print(MiClase.variable_clase2)
#Se puede acceder desde los objetos tambien
print(ObjEjemplo.variable_clase2)
print(ObjEjemplo2.variable_clase2)

#Accediendo a variable de clase por medio de un objeto
MiClase.metodo_clase()
ObjEjemplo3 = MiClase('Variable_instancia')
ObjEjemplo3.metodo_clase()
print('-'.center(50,'-'))
ObjEjemplo3.metodo_instancia()







