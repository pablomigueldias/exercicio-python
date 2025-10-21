#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um
#dicionario e todos os dicionarios em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Um lista com todas as mulhueres
#D) Uma lista com todas as pessoas com idade acima de média

lista = []
while True:
    pessoas = {}
    pessoas['nome'] = str(input('Nome: ')).capitalize().strip()
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas)
    condicao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while condicao not in 'SN':
        print('Condição invalida, tente novamente...')
        condicao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if condicao == 'N':
        break

soma = 0
for c in range(0,len(lista)):
    soma += lista[c]['idade']
media = soma / len(lista)


print(f'- O grupo tem {len(lista)} pessoas')
print(f'- A media de grupo é {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(f'{lista[c]['nome']}', end=' ')
print('\n')
print('=='*30)
print('Lista de pessoas acima da média')
for c in range(0, len(lista)):
    if lista[c]['idade'] > media:
        print(f'nome = {lista[c]['nome']} sexo = {lista[c]['sexo']} idade = {lista[c]['idade']}')



