# Faça um programa que leia um numero inteiro e diga se ele é primo ou nao

numero = int(input('Digita um numero inteiro: '))

primos = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[33m{c}\033[m')
        primos = primos + 1
    else:
        print(f'{c}')

if primos == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} nao é primo')
