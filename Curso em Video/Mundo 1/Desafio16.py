#Crie um programa que leia um numero real qualquer pelo teclado
# e mostre na tela sua porção inteira.
from math import trunc

numero = float(input('Digite um numero: '))
arrendo = trunc(numero)

print(f'o numero tem a {numero} tem a parte inteira {arrendo}')