# faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando
# jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

import random

computador = random.randint(1, 5)
vitoriaU = 0

while True:
    usuario = int(input('Digite um numero inteiro: '))
    condicao = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    soma = computador + usuario
    if condicao == 'P':
        if soma % 2 == 0:
            print(f'A soma de {usuario} + {computador} = {soma}. Deu PAR')
            print('Voce Ganhou')
            print('Tente Novamente')
            vitoriaU = vitoriaU + 1
        else:
            print(f'A soma de {usuario} + {computador} = {soma}. Deu IMPAR')
            print('Voce Perdeu')
            break
    if condicao == 'I':
        if soma % 2 == 1:
            print(f'A soma de {usuario} + {computador} = {soma}. Deu IMPAR')
            print('Voce Ganhou')
            print('Tente Novamente')
            vitoriaU = vitoriaU + 1
        else:
            print(f'A soma de {usuario} + {computador} = {soma}. Deu PAR')
            print('Voce Perdeu')
            break
print(f'Game Over! Você venceu {vitoriaU} vezes.')
