#refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for

numero = int(input('Qual tabuada voce quer que eu gere? '))

print (f'Tabuada do {numero}')

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} X {i:2} = {resultado}')