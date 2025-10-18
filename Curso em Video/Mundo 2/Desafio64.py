#crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quanto o
# usuario digitar o valor 999, que é a condição de parada. no final mostre quantos numeros
#foram digitados e qual foi a soma entre eles.

numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input('Digita um numero: '))
    if numero != 999:
        soma = soma + numero
        contador += 1

print(f'Foram {contador} numeros e a soma deles é {soma}')

