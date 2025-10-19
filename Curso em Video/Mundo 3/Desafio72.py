# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# seu programa deverá ser um numero pelo teclado (entre 0 e 20) e mostrá-lo por estenso.

numeros_por_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte"
)
n = int(input('Digite um numero inteiro de 0 até 20: '))

while n < 0 or n > 20:
    n = int(input('Digite um numero inteiro de 0 até 20: '))

for c in range(0, len(numeros_por_extenso)):
    print(f'Voce digitou o numero {numeros_por_extenso[n]}')
    break

