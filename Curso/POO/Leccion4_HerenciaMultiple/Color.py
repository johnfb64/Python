"""
Revisar comentarios en clase FiguraGeometrica
"""
class Color:
    def __init__(self,color):
        self._color = color

    @property
    def color(self,color):
        return self._color

    @color.setter
    def color(self,color):
        self._color

    def __str__(self):
        return f'Color[color:{self._color}]'
