#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.Guarde esses
#resultados em um dicionario. No dinal coloque esse dicionario em ordem, sabendo que o vencedor tirou o 
#maior numero dado.

from operator import itemgetter
from random import randint
from time import sleep

jogo = {
    'Jogador 1': randint(1,6),
    'Jogador 2': randint(1,6),
    'Jogador 3': randint(1,6),
    'Jogador 4': randint(1,6)
}

for jogador, valor in jogo.items():
    print(f'{jogador} tirou {valor}')
    sleep(1)

rank = sorted(jogo.items(),key=itemgetter(1),reverse=True)

print('Ranking dos jogadores')

for pos,(jogador,valor) in enumerate(rank, start=1):
    print(f'{pos}º lugar: {jogador} tirou: {valor}')
    sleep(1)
