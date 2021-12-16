class Monitor:

    contadorMonitores = 0

    def __init__(self,marca,tamano):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamano = tamano

    @property
    def idMonitor(self):
        return self._idMonitor

    @idMonitor.setter
    def idMonitor(self,idMonitor):
        self._idMonitor = idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self,tamano):
        self._tamano = tamano


#Test
    def __str__(self):
        return f'Id Monitor: {self.idMonitor}, Marca: {self.marca}, Tamaño: {self.tamano}'

if __name__ == '__main__':
    test = Monitor('Asus','22"')
    print(test)


