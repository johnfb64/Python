from MundoPC.Monitor import Monitor
from MundoPC.Mouse import Mouse
from MundoPC.Teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    def __init__(self,nombre,monitor,teclado,mouse):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    @property
    def idComputadora(self):
        return self._idComputadora

    @idComputadora.setter
    def idComputadora(self,idComputadora):
        self._idComputadora = idComputadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self,monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self,teclado):
        self._teclado = teclado

    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self,mouse):
        self._mouse = mouse

    def __str__(self):
        return f'''
        Hostname: {self.nombre}
        Id Computador: {self.idComputadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Mouse: {self.mouse}    
        '''


#Test
if __name__=='__main__':
    mouse1 = Mouse('laser','HP')
    teclado1 = Teclado('Mecanico','Redragon')
    monitor1 = Monitor('Lenovo', '22 pulgadas')
    pc1 = Computadora('PC Master Race', monitor1, teclado1, mouse1)
    print(pc1)

    mouse2 = Mouse('clasico', 'Logi')
    teclado2 = Teclado('Membrana', 'Generico')
    monitor2 = Monitor('Asus', '38 pulgadas')
    pc2 = Computadora('Oficina', monitor2, teclado2, mouse2)
    print(pc2)







