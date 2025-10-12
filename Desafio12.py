#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

numero = float(input('Qual é o preço do produto? R$ '))
desconto = numero * 0.05
total = numero - desconto

print(f'O produto com 5% de desconto é R${total}')