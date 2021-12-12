class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

#Sobrecarga de operacion add o suma
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad



persona1 = Persona('John',39)
persona2 = Persona('Fernando',74)
print(persona1 + persona2)
print(persona2 - persona1)
