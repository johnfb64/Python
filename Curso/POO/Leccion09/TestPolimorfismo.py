"""
Explicacion: Tengo dos clases una tipo empleado (padre) y gerente (hija). Necesito crear objetos y que cada objeto
sepa a que metodo referirse, si en este caso a la clase gerente o clase empleado. Esto por que podrian existir muchas
mas cargos en la empresa, pero el objeto necesitara saber que metodo o metodos utilizar, sin necesidad que se le este
haciendo referencia a que metodo deberia dirigirse.

Crear un metodo donde se almacene el objeto permitira acceder al __str__ de esa clase y este caso indicar el tipo.
El metodo sabra a que metodo se estan refiriendo por que al momento de crear el objeto se le dice que que tipo de clase
es.

"""

from Empleado import Empleado
from Gerente import Gerente


def imprmir_detalles(objeto):
    print(objeto)
    #Este print indica a que objeto apunta en tiempo de ejecución
    print(type(objeto))
    #Este if garantiza que el objeto al que se apunta en tiempo de ejecución es el adecuado. En este cao solo permitira
    #y confirmara datos del objeto tipo Gerente para posteriormente acceder a su metodo departamento.
    if isinstance(objeto,Gerente):
        print(objeto.departamento)


#Variable que apunta a clase padre
empleado1 = Empleado('Juan', 5000)
imprmir_detalles(empleado1)

gerente1 = Gerente('Carolina', 6000, 'Sistemas')
imprmir_detalles(gerente1)
#comentario de prueba para test de git

