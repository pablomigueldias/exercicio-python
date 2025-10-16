# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento

# - à Vista dinheiro/cheque: 10% de desconto
# - à Vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão 20% de juros

valor = float(input('Digite o valor do produto: R$ '))
print('-='*50)
print('1- À Vista Dinheiro/Cheque | 2- À Vista no cartão | 3- 2x no cartão | 4- 3x ou mais no cartão')
print('-='*50)

condicao = int(input('Qual a condicao? : '))

if condicao == 1:
    desconto = valor * 0.10
    total = valor - desconto
    print(f'O produto de R${valor} teve um desconto de 10% que ficou {total}')
elif condicao == 2:
    desconto = valor * 0.05
    total = valor - desconto
    print(f'O produto de R${valor} teve um desconto de 5% que ficou {total}')
elif condicao == 3:
    print(f'O produto de R${valor} nao teve desconto e ficou {valor}')
elif condicao == 4:
    parcela = int(input('Quantas vezes?: '))
    juros = valor * 0.20
    total = valor + juros
    print(f'Em {parcela}x teve um juros de 20% no total R${total}')
