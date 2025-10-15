#Crie um progama que leia um numero inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Digite um numero inteiro: '))

if numero % 2 == 1:
    print('O seu numero é impar')
else:
    print('Seu numero é par')