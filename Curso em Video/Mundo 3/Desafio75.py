#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
#A)Quantas vezes apareceu o valor 9.
#B)em que posição foi digitado o valor 3
#C)Quais foram os numeros pares

numeros = (int(input('Digite um numero: ')), 
           int(input('Digite um numero: ')), 
           int(input('Digite um numero: ')), 
           int(input('Digite um numero: ')))


print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posição')

print('Os valore pares digitados foram ', end='')

for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0 :
        print(f'{numeros[c]}', end=' ')