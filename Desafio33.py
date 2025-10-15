#Faça um progama que leia três numeros e mostre qual é o maior e qual é o menor

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))


maior = max(numero1,numero2,numero3)
menor = min(numero1,numero2,numero3)

print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')
