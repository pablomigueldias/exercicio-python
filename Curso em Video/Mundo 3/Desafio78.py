# faça um programa que leia 5 valores numericos e guarde os em uma lista
# no final, mostre qual foi o maior e o menor valore digitado e as suas respectivas posições na lista

numeros = []

for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {c}: ')))

maior = max(numeros)
menor = min(numeros)

print(f'Voce digitou os valores {numeros}')

print(f'O maior numero foi {maior} nas posições', end=' ')
for c in range(0, len(numeros)):
    if numeros[c] == maior:
        print(f'{c}...', end=' ')

print(f'\nO menor numero foi {menor} nas posições', end=' ')
for c in range(0, len(numeros)):
    if numeros[c] == menor:
        print(f'{c}...', end=' ')
