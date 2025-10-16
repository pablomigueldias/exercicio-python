# Faça um programa que leia o ano de nascimento de um jovem e informe. de acordo com sua idade
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se ja passou do tempo de alistamento

# seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo

import datetime

anoAtual = datetime.datetime.now().year

ano = int(input('Qual ano que voce nasceu? : '))

resultado = anoAtual - ano
anoAlista = ano + 18
tempoFalta = anoAtual - anoAlista

if resultado == 18:
    print(
        f'Voce esta na idade de se alistar que sera em {anoAlista} e o tempo que falta é {tempoFalta} anos')
elif resultado > 18:
    print(
        f'Voce voce ja se alistou que foi no ano {anoAlista} e ja faz {tempoFalta} anos')
elif resultado < 18:
    tempoFalta = anoAlista - anoAtual
    print(
        f'Voce nao se alistou seu ano será {anoAlista} e falta {tempoFalta} anos')
