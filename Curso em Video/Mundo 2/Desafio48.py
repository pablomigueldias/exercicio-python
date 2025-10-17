#Faça um programa que calcule a soma entre todos os numerros impares que são multiplos de 3
# e que se encontram no intevalo de 1 até 500

soma = 0
contador = 0
for c in range (1,501):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print(f'A soma de todos os {contador} valores solicitados é {soma}')
