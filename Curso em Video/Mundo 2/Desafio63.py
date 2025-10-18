# Escreva um programa que laia um numero n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma sequencia fibonacci
# Ex: 0,1,1,2,3,5,8

n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
contador = 3

print(f'{t1} -> {t2}', end=' -> ')

while contador <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    contador += 1
print('Fim')
