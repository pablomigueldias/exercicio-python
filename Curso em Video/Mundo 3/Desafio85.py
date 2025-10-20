#crie um programa onde o usuário possa digitar sete valores numerico e cadastre-os em uma lista
#unica que mantenha separados os valores pares e impares. no final, mostre os valores pares
#impares em ordem crescente

numeros = [[],[]]

for c in range(0, 7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    elif numero % 2 == 1:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(f'O valores pares digitador foram: {numeros[0]}')
print(f'O valores impares digitador foram: {numeros[1]}')



