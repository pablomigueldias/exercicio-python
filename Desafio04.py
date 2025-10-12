# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

algo = input('Digite algo = ')

print(f'isso é alfabetico numerico? {algo.isalnum()}')
print(f'isso esta em maiuculo? {algo.isupper()}')
print(f'isso esta no alfabeto? {algo.isalpha()}')
print(f'isso é um numerico? {algo.isnumeric()}')
print(f'Qual tipo primitivo? {type(algo)}')
