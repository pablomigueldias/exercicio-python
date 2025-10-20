#faça um programa que ajuda um jogador da mega sena cirar palpites. o programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para casa jogo, cadastrado
# tudo em uma lista composta.
from random import randint
from time import sleep


palpite = int(input('Quantos palpites voce quer?: '))
palpites = []
dados = []

for c in range(0, palpite):
    for c in range(0,6):
        numero = randint(1,60)
        if numero not in dados:
            dados.append(numero)
        elif numero in dados:
            numero = randint(1,60)
            dados.append(numero)
    palpites.append(dados[:])
    dados.clear()

for c in range(0, len(palpites)):
    print(f'Jogo {c+1}: {palpites[c]}')
    sleep(1)


