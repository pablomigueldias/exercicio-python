#faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Qual tabuada voce quer que eu gere? '))

print (f'Tabuada do {numero}')

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')