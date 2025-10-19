#Crie um programa que vai gerar cinco numeros aleatórios e colocar em um tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior
# valor que estão na tupla.

from random import randint

computador = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: {computador}')
print(f'O maior valor sorteado foi: {max(computador)}')
print(f'O menor valor sorteador foi: {min(computador)}')