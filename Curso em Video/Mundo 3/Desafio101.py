#Crie um programa quie tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma péssoa tem voto negado. opcional ou obrigatório
# nas eleições.

import datetime


def voto(ano):
    anoAtual = datetime.datetime.now().year
    idade = anoAtual - ano

    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO NÃO OBRIGATÓRIO'



ano = int(input('Em que ano voce nasceu?: '))
print(voto(ano))
