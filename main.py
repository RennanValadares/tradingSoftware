#coding: utf-8

import Funcs  # EXCEPTION FUNCTIONS
import FRETE  # LOGISTIC COST
import ICMS   # Tax Calculation


fretecomp = 0
fretevend = 0
sacos = 0

# __________________________________________LOGISTICS COST______________________________________________________________

# LOGISTIC COST WHEN BUYING

fcomp = str(input('Possuí frete de compra? [S] ou [N]'))
soun = ('S', 's', 'SIM', 'Sim', 'sim','N', 'n', 'NÃO', 'Não', 'não')
s = ('S', 's', 'SIM', 'Sim', 'sim')
n = ('N', 'n', 'NÃO', 'Não', 'não')
while fcomp not in soun:
    print('Responda com S ou N')
    fcomp = str(input('Possuí frete de compra? [S] ou [N]'))

if fcomp in s:
    sacos = Funcs.scs('Qual a Quantidade de Sacos?')
    valorf = Funcs.peso('Qual o valor do Frete por Tonelada ?')
    r1 = FRETE.Frete()
    r1.scs = sacos
    r1.vlrf = valorf
    print(r1.cfrete(r1._scs, r1._vlrf ))

# LOGISTIC COST WHEN SELLING

fvend = str(input('Possuí frete de venda? [S] ou [N]'))

while fvend not in soun:
    print('Responda com S ou N')
    fcomp = str(input('Possuí frete de compra? [S] ou [N]'))

if fvend in s:
    sacos = Funcs.scs('Qual a Quantidade de Sacos?')
    valorf = Funcs.peso('Qual o valor do Frete por Tonelada ?')
    r2 = FRETE.Frete()
    r2.scs = sacos
    r2.vlrf = valorf
    print(r2.cfrete(r2._scs, r2._vlrf))

# ______________________________________________ICMS TAX COST___________________________________________________________

# Buying ICMS cost
estadoe = Funcs.ent(input('Qual estado de compra dos grãos ? (GO, DF ou MG)'))
estados = Funcs.ent(input('Para qual filial ? (GO ou MG)'))
precoprod = Funcs.preco()
ativ = Funcs.ativ(input('Qual a atividade ? (Produtor, Cooperativa ou Cerealista)'))
pror = Funcs.pror(input('O Produtor Possuí Pro Rural ?'))
z = ('DF', 'Df', 'df')
pro = ('PRODUTOR', 'Produtor', 'produtor')
imp = ICMS.Icms()
imp.imposto(estadoe, estados, precoprod, ativ, pror)
print(imp.icmscomp)

#


