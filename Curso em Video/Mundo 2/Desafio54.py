#Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas ja são maioes.

import datetime

maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Qual seu ano de nascimento?: '))
    idade = datetime.datetime.now().year - ano
    if idade < 21:
        menor = menor + 1
    elif idade >= 21:
        maior = maior + 1

print(f'Dos 7: {maior} são maior de idade')
print(f'Dos 7: {menor} são menor de idade')