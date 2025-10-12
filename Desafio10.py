# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre auntos dolares ela pode comprar.

carteira = float(input('Quanto dinheiro voce tem na carteuira? R$ '))
dolar =  carteira * 5.53


print(f'Voce tem R${carteira}.')
print(f'Voce pode comprar ${dolar:2f} dolares')