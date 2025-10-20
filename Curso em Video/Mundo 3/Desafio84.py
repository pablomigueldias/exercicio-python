# Faça um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. no final
# mostre

# A) quantas pessoas foram cadastradas.
# B) uma listagem com as pessoas mais pesadas
# C) uma listagem com as pessoas mais leves


dado = []
pessoas = []
qtdpessoas = 0
maior = []
menor = []


while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    qtdpessoas = qtdpessoas + 1
    dado.clear()

    condicao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while condicao not in 'SN':
        print('Valor invalido, tente novamente..')
        condicao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if condicao == 'N':
        break

maior = [pessoas[0]]
menor = [pessoas[0]]
maiorPeso = pessoas[0][1]
menorPeso = pessoas[0][1]

for nome, peso in pessoas[1:]:

    if peso > maiorPeso:
        maiorPeso = peso
        maior = [[nome, peso]]
    elif peso == maiorPeso:
        maior.append([nome,peso])

    if peso < menorPeso:
        menorPeso = peso
        menor = [[nome,peso]]
    elif peso == menorPeso:
        menor.append([nome,peso])


print(f'Ao todo, voce cadastrou {qtdpessoas} pessoas')
print(f'O maior peso foi de {maiorPeso}. de ', end=' ')
for m in maior:
    print(f'{m[0]}', end=', ')
print(f'\nO menor pedo foi de {menorPeso}. de ', end=' ')
for m in menor:
    print(f'{m[0]}', end=', ')
