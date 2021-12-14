from Empleado import Empleado
def imprmir_detalles(objeto):
    print(objeto)
    #Este print indica a que objeto apunta en tiempo de ejecución
    print(type(objeto))



empleado1 = Empleado('Juan', 5000)
imprmir_detalles(empleado1)