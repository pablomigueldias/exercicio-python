#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá
#perguntar se o usário quer ou nao continuar. No final mostre:

#Quantos pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados.
#Quantas mulheres tem menos de 20 anos

qtdPessoas = 0
qtdHomens = 0
qtdMulheres = 0

while True:
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Qual seu sexo:  ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Valor invalido...')
        sexo = str(input('Qual seu sexo:  ')).strip().upper()[0]
    if idade > 18:
        qtdPessoas = qtdPessoas + 1
    if sexo == 'M':
        qtdHomens = qtdHomens + 1
    if sexo == 'F' and idade < 20:
        qtdMulheres = qtdMulheres + 1
    condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while condicao not in 'SN':
        print('Valor invalido...')
        condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if condicao == 'N':
        break
    

print(f'Quantidade de pessoas com mais de 18 anos: {qtdPessoas}')
print(f'Quantidade de homens cadastradoos: {qtdHomens}')
print(f'Quantidade de mulheres com menos de 20 anos cadastrado: {qtdMulheres}')
