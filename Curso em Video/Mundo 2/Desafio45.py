# Crie um progama que faça o computador jogar jokenpo com voce.

import random

print('JokenPô')
print('0 - Pedra | 1 - Papel | 2 - Tesoura')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

usuario = int(input('Digite um numero: '))

print(f'Computador tirou:  {itens[computador].upper()}')
print(f'Usuário tirou:  {itens[usuario].upper()}')

if computador == 0:
    if usuario == 0:
        print('Empate!')
    elif usuario == 1:
        print('O Usuário venceu!')
    elif usuario == 2:
        print('O Computador venceu!')

elif computador == 1:
    if usuario == 0:
        print('O Computador venceu!')
    elif usuario == 1:
        print('Empate!')
    elif usuario == 2:
        print('O Usuário venceu!')

elif computador == 2:
    if usuario == 0:
        print('O Usuário venceu!')
    elif usuario == 1:
        print('O Computador venceu!')
    elif usuario == 2:
        print('Empate!')
