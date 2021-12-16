from MundoPC.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    #No se debe declara el incializador, contadorTeclados es una variable de CLASE.
    contadorTeclados = 0

    def __init__(self, tipo, marca):
        super().__init__(tipo, marca)
        Teclado.contadorTeclados += 1
        #self._idTeclado = idTeclado
        self._idTeclado = Teclado.contadorTeclados

    @property
    def idTeclado(self):
        return self._idTeclado

    @idTeclado.setter
    def idTeclado(self, idTeclado):
        self._idTeclado = idTeclado

#Test
    def __str__(self):
        return f'Id Teclado: {self.idTeclado},{super().__str__()}'


if __name__ == '__main__':
    test = Teclado('Mouse','HP')
    print(test)
    test1 = Teclado('Mouse', 'ReDragon')
    print(test1)
