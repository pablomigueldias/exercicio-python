# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = input('Digite o numero de 0 a 9999: ').zfill(4)

print(f'Unidades {numero[3]}')
print(f'Dezena {numero[2]}')
print(f'Centena {numero[1]}')
print(f'milhar {numero[0]}')




