# coding: utf-8

# EXEPTION FOR INT INPUT ON sacos

import numbers
def scs(num):
    while True:
        try:
            return int(input(num))
        except:
            print('Valor de Sacos Inválido')

# EXEPTION FOR FLOAT INPUT ON valorf


def peso(num):
    while True:
        try:
            return float(input(num))
        except:
            print('Valor do Frete por Tonelada Inválido.')

# EXEPTIONS FOR ICMS ENTRADA


def ent(num):
    x = ('GO', 'Go', 'go', 'MG', 'Mg', 'mg', 'DF', 'Df', 'df')
    while num not in x:
        print('Estado de Entrada Incorreto: {}'.format(num))
        num = input('Qual o estado de Entrada?')


# EXEPTIONS FOR ICMS SAIDA


def sai(num):
    x = ('AC', 'Ac', 'ac', 'AL', 'Al', 'al', 'AP', 'Ap', 'ap', 'AM', 'Am', 'am', 'BA',
         'Ba', 'ba', 'CE', 'Ce', 'ce', 'DF', 'Df', 'df', 'ES', 'Es', 'es', 'GO', 'Go',
         'go', 'MA', 'Ma', 'ma', 'MT', 'Mt', 'mt', 'MS', 'Ms', 'ms', 'MG', 'Mg', 'mg',
         'PA', 'Pa', 'pa', 'PB', 'Pb', 'pb', 'PR', 'Pr', 'pr', 'PE', 'Pe', 'pe', 'PI',
         'Pi', 'pi', 'RJ', 'Rj', 'rj', 'RN', 'Rn', 'rn', 'RS', 'Rs', 'rs', 'RO', 'Ro',
         'ro', 'RR', 'Rr', 'rr', 'SC', 'Sc', 'sc', 'SP', 'Sp', 'sp', 'SE', 'Se', 'se',
         'TO', 'To', 'to')

    while num not in (x):
        print('Estado de Saída Incorreto: {}'.format(num))
        num = input('Qual estado de Saída ?')
    while True:
        try:
            return str(input(num))
        except:
            print('Estado de Saída Inválido: {]'.format(num))

# EXEPTION FOR PRECO


def preco():

  # while isinstance(num, numbers.Real) == False:
  #       print('Valor de Compra Pago ao Produtor Inválido.')
  #       num = input('Qual o preço de compra liquido pago ao produtor ?')

    while True:
        try:
            return float(input('Qual o preço de compra liquido pago ao produtor ?'))
        except:
            print('Valor de Compra Pago ao Produtor Inválido.')

# EXEPTION FOR ATIV

def ativ(num):
    x = ('PRODUTOR', 'Produtor', 'produtor', 'CEREALISTA', 'Cerealista', 'cerealista', 'COOPERATIVA', 'Cooperativa',
         'cooperativa')
    while num not in x:
        print('Atividade Incorreta. Escolha entre: Produtor, Cooperativa ou Cerealista')
        num = input('Qual a atividade do Produtor?')


# EXEPTION FOR PRO RURAL

def pror(num):
    x = ('SIM','sim','Sim', 'NÃO', 'Não', 'não', 'NAO', 'Nao', 'nao', 'n', 's', 'N', 'S')
    while num not in x:
        print('Responda com Sim ou Não.')
        num = input('O produtor possuí Pro Rural?')


