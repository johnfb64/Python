"""
Linea 8-11. Denfine los atributos de la clase
Linea 13 y 21. @property Define el getter por medio del decorador property. regresa atributo de ancho. Regresa valores
                con atributos encapsulados.
Linea 17 y 25. @atributo.setter Define el setter por medio del decorador setter. No regresa nada, solo modifica atributo ancho
Linea 29. __str__ permite sobreescritura de atributos
"""

#ABC = Abstract Base Class - abstractmethod = importa decorador y define metodos abstractos.
from abc import ABC, abstractmethod

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        #Validación por medio de metodo (ver linea 46, ultima seccion)
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo: {ancho}')
        #Validacion por medio de if
        if 0 < alto < 10:
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    #Decorador para declara metodos abstractos.
    @abstractmethod
    def calcular_area(self):
        pass # pass indica que no tiene metodos, deja pasar.


    def __str__(self):
        return f'Figura Geometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    #metodo encapsulado de validación

    def _validar_valor(self,valor):
        #Notacion simplificada
        return True if 0 < valor < 10 else False
