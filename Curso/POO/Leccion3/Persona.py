"""
-----------------HERENCIA DE OBJETOS-----------------------
- Creacion de clases
- Creacion de objetos



-----------------------------------------------------------
"""
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
# __str__ Sobreescribe metodo de clase padre.
    def __str__(self):
        return f'Persona: {self.nombre, self.edad}'

#Se crea clase Empleado que hereda de persona, en este caso se define entre parentesis el padre

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        #SUPER es necesario para que se puedan acceder a los metodos y atributos heredados del padre
        #__init__ tambien es necesario para acceder a los atributos heredados.
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    #Se define memtodo de sobreescritura
    def __str__(self):
        #Se manda a llamar al metodo de sobre escritura con super de la clase padre a la hija
        return f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1 = Empleado('John', 39, 4000000)

print(f'El empleado es {empleado1.nombre}, tiene {empleado1.edad} años y se gana {empleado1.sueldo} al mes')