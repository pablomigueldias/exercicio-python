#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem
#pares. se o valor digitado for impar desconsidere

soma = 0
contador = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c} valor: '))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print(f'A soma de todos os numeros pares é {soma}')
