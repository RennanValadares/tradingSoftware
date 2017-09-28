#coding: utf-8

# CALC THE ICMS TAX

#_________________________________________________ICMS WHEN BUYING_____________________________________________________
class Icms():
    def __init__(self):
        self._entrada = 0
        self._saida = 0
        self._tipo = 0
        self.icmscomp = 0
        self.icmsvend =0
        self.precocomp = 0

    @property
    def entrada(self):
        return  self._entrada

    @entrada.setter
    def entrada (self, num):
        if(not(isinstance(num, str))):
            raise ValueError('Estado de entrada inválido: {}'.format(num))
        self._entrada = str(num)

    @property
    def saida(self):
        return self.saida

    @saida.setter
    def saida(self, num):
        if not (isinstance(num, str)):
            raise ValueError('Estado de entrada Inválido: {}'.format(num))
        self._saida = num

# _____________________________________________ICMS BUYING TAX_________________________________________________________
    def imposto(self, estadoe, estados, precoprod, ativ, pror):
        x = ('GO', 'Go', 'go')
        y = ('MG', 'Mg', 'mg')
        z = ('DF', 'Df', 'df')
        pro = ('PRODUTOR', 'Produtor', 'produtor')
        co = ('COOPERATIVA', 'Cooperativa', 'cooperativa')
        ce = ('CEREALISTA', 'Cerealista', 'cerealista')
        prors = ('SIM', 'Sim', 'sim', 'S', 's')





        #MG - GO OR GO - MG (ERROR)
        while ((estadoe in x) and (estados in y)):
            print("Estado de destino incorreto!")
            estadoe = input("Qual estado de compra dos grãos ? (GO, DF ou MG)")
            estados = input('Para qual filial ? (GO ou MG)')


        # GO - GO AND MG - MG PRODUTOR OR COOPERATIVA
        if ((estadoe in x) and (estados in x) and (ativ in pro or co)) or ((estadoe in y) and (estados in y) and (ativ
                                                                                                                  in
                                                                                                                  pro
                                                                                                                  or co
                                                                                                                  )):
            self.icmscomp = 0

        # GO - GO CEREALISTA
        elif (estadoe in x) and (estados in x) and (ativ in ce):
            self.icmscomp = precoprod * 0.17

        # DF - GO OR DF - MG (WITH PRO RURAL)
        elif (estadoe in z) and ((estados in x)or (estadoe in y)) and (ativ in pro) and (pror in prors):
            self.icmscomp = precoprod * 0.024

        # DF - GO OR DF - MG (WITHOUT PRO RURAL)
        elif (estadoe in z) and ((estados in x)or (estadoe in y)):
            self.icmscomp = precoprod * 0.12

        # MG - MG CEREALISTA
        elif (estadoe in y) and (estados in y) and (ativ in ce):
            self.icmscomp = precoprod * 0.18
















