# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um numero inteiro: '))

contador = numero
fatorial = 1

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print(f'Fatorial de {numero} é {fatorial}')
