class Persona:
    #Variable de clase
    contador_personas = 0

    @classmethod
        #Metodo de clase. Se asigna cls para acceder a variables de clase.
    def generar_siguiente_valor(cls):
        # Contador personas incrementara en 1 cada vez que se cree un objeto
        cls.contador_personas += 1
        return cls.contador_personas


    def __init__(self,nombre,edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan',28)
print(persona1)
persona2 = Persona('John',39)
print(persona2)
persona3 = Persona('Elvira',34)
print(persona3)
#Se puede incrementar por aparta el contador mandando a llamar el metodo:
Persona.generar_siguiente_valor()
persona4 = Persona('Pepa',15)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')
