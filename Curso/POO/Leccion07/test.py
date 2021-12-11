from Orden import Orden
from Producto import Producto

producto1 = Producto('Disco Duro', 200000)
producto2 = Producto('CPU', 500000)
producto3 = Producto('RAM', 420000)
producto4 = Producto('Chasis', 400000)
producto5 = Producto('Fuente',300000)

productos1 = [producto1, producto2, producto3]
orden1 = Orden(productos1)
print(orden1)
productos2 = [producto1, producto2]
orden2 = Orden(productos2)
print(orden2)
productos3=[producto4,producto5]
orden3 = Orden(productos3)
print(orden3)
print('')

print(f'Total de Orden 1: {orden1.calcular_total()}')
print(f'Total de Orden 2: {orden2.calcular_total()}')
print(f'Total de Orden 3: {orden3.calcular_total()}')

orden1.agregar_producto(producto4)
orden1.agregar_producto(producto5)

print(orden1)
print(f'Nuevo Total de Orden 1: {orden1.calcular_total()}')