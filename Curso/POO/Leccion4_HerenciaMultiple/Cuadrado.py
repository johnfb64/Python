"""
Esta clase es la hija de FiguraGeometrica y Color.
Linea 13 y 14. Hace importaciones de clases padre
Linea 17. La clase cuadrado se inicia con el sefl, lado y color. Lado sera el parametro ancho o alto de FiguraGeometica.
Linea x. Inicializa atributos de FiguraGeometrica - En esta parte lado se utiliza solo para inicializar alguna de las variables,
         no es necesario hacerla llamar en el metodo
Linea x. Inicializa atributos de Color
Linea x. Los atributos del metodo calculular_area son de la clase padre FiguraGeometrica
Linea 25. Sobreescribe los metodos heredados de clase padre.
Linea 26. Manda a llamar en un "fstring"  el metodo de clase padre y se declara como self, ya que esta en la misma clase.
"""

# Clase Hija
from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
