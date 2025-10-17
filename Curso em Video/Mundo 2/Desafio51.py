#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre
#os 10 primeiros termos dessa progressão.
# formula an​=a1​+(n−1)⋅r

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))

for n in range(1,11):
    termo = a1 + (n - 1)* r
    print(f'{n}º : {termo}')