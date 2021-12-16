from MundoPC.Teclado import DispositivoEntrada


class Mouse(DispositivoEntrada):

    contadorRatones = 0

    def __init__(self, tipo,marca,):
        super().__init__(tipo, marca)
        Mouse.contadorRatones += 1
        self._idRaton = Mouse.contadorRatones

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self,idRaton):
        self._idRaton = idRaton

#test
    def __str__(self):
        return f'id Mouse: {self.idRaton},{super().__str__()}'


if __name__=='__main__':
    test1 = Mouse('Mouse','Logi')
    print(test1)



