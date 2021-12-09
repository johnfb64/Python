"""
Ver comentarios de clase Cuadrado.py

"""

from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, base, altura, color):
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'