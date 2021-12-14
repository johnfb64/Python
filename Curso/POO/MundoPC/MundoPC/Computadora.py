class Computadora:
    contadorComputadoras = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras

