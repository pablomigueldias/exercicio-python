#Faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e o menor
# peso lidos

pesos = []

for c in range(1,6):
    peso = float(input('Qual o peso? : '))
    pesos.append(peso)

minimo = min(pesos)
maximo = max(pesos)

print(f'O que tem maior peso é {maximo}')
print(f'O que tem menor peso é {minimo}')

