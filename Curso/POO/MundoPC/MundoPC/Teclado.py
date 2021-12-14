from MundoPC.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    def __init__(self,idTeclado,tipo,marca):
        super().__init__(self,tipo,marca)
        self.contadorTeclados += 0
        self._idTeclado = idTeclado


    @property
    def idTeclado(self):
        return self._idTeclado

    @idTeclado.setter
    def idTeclado(self,idTeclado):
        self._idTeclado = idTeclado
#Test
    def __str__(self):
        return f'IdTeclado: {self.idTeclado}, {super.__str__()}'

if __name__ == '__main__':
    test = DispositivoEntrada('001','Mouse','HP')
    print(test)