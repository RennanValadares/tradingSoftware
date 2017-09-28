#coding: utf-8

#class to calculate the logistcs cost on Buying or Selling


class Frete():
    def __init__(self):
        self._fretescs = 0
        self._frt = 0
        self._scs = 0
        self._vlrf = 0

    @property
    def scs(self):
        return self._scs

    @scs.setter
    def scs(self, num):
        if(not(isinstance(num, int))):
            raise ValueError('Quantidade de Sacos Inválida: {}'.format(num))
        self._scs = num

    @property
    def vlrf(self):
        return self.vlrf

    @vlrf.setter
    def vlrf(self, num):
        if(not(isinstance(num, float))):
            raise ValueError('Preço Inválido: {}'.format(num))
        self._vlrf = num

    def cfrete (self, _scs, _vrlf):
        return (self._vlrf / 16.6666666666667) * self._scs




