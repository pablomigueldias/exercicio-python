# Melhores o jogo do Desafio 028 onde o computador vai 'Pensar' em um numero entre 0 e 10 só que agora o jogador vai tentar#
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

computador = random.randint(1, 10)

usuraio = int(input('Adivinhe o numero que estou pensando de 1 até 10 : '))

contador = 0
while usuraio != computador:
    usuraio = int(input('Voce errou tente novamente: '))
    contador = contador + 1

print(f'Voce venceu mas tentou {contador+1} vezes para vencer ')
