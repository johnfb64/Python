from MundoPC.Teclado import DispositivoEntrada


class Mouse(DispositivoEntrada):

    contadorRatones = 0

    def __init__(self, idRaton):
        self.contadorRatones +=1
        self._idRaton = idRaton



