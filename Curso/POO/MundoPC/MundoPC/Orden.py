from MundoPC.Computadora import Computadora


class Orden:
    contadorOrdenes = 0
    def __init__(self,computadoras):
        Orden.contadorOrdenes +=1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras

    @property
    def idOrden(self):
        return self._idOrden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self,computadoras):
        self._computadoras = computadoras

    def AgregarComputadoras(self,computador):
        self.computadoras.append(computador)



    def __str__(self):
        computadoras_str = ''
        for computadoras in self.computadoras:
            computadoras_str += Computadora.__str__()
        f'''
        Orden: {self.idOrden}
        Computadoras: {computadoras_str}

        '''

