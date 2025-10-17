#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem
#pares. se o valor digitado for impar desconsidere

soma = 0
for c in range(1,7):
    if c % 2 == 0:
        print(c)
        soma = soma + c
print(f'A soma de todos os numeros é {soma}')
