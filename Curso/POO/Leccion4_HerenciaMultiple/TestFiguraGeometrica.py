"""
linea x. Adornos del programa para deliminitar resultados
"""

from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(3,'azul')
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación de objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(4,5,'rojo')
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#No se puede inicializar una clase abstracta.
#figura = FiguraGeometrica()

