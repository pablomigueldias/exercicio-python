#A Confederação nacional de natação precisa de um programa que laia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: Mirim
#- Até 14 anos: Infantil
#- Até 19 anos: Junior
#- Até 20 anos: Sênior
#- Acima: Master

import datetime

ano = int(input('Digite o seu ano de nascimento YYYY: '))
anoAtual = datetime.datetime.now().year

idade = anoAtual - ano

if idade <= 9:
    print('Você é MIRIM')
elif idade <= 14:
    print('Voce é INFANTIL')
elif idade <= 19:
    print('Voce é JUNIOR')
elif idade <=20:
    print('Voce é SENIOR')
else:
    print('Voce é Master')