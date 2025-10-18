#Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se
#o usuario vai continuar. No final, mostre

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

soma = 0
qtdproduto = 0
nomeBarato = ''
produtoBarato = 0

while True:
    produto = str(input('Qual o nome do produto: ')).strip().upper()
    preco = float(input('Qual o preço: '))

    soma = soma + preco
    if preco > 1000:
        qtdproduto = qtdproduto + 1
    if produtoBarato == 0 or preco < produtoBarato:
        nomeBarato = produto
        produtoBarato = preco

    condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while condicao not in 'SN':
        print('Valor invalido...')
        condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if condicao == 'N':
        break

print(f'O total de compra foi R${soma:.2f}')
print(f'Temos {qtdproduto} produtos custando mais de R$1000.00')
print(f'O Produto mais barato foi {nomeBarato} que custa R${produtoBarato:.2f}')
