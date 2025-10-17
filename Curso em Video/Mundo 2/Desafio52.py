#Faça um programa que leia um numero inteiro e diga se ele é primo ou nao

numero = int(input('Digita um numero inteiro: '))

primos = 0

for c in range(1,numero +1):
    if numero % c == 0 and c == 2:
        primos = primos + 1

if primos == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} nao é primo')