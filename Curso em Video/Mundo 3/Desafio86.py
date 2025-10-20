#Crie um programa que cire uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# no final mostre a matriz na tela coma formatação correta

matriz = []

for c in range(1,10):
    valor = int(input(f'Digite {c} valor : '))
    matriz.append(valor)

for c in range(0,len(matriz), 3):
    print(f'[{matriz[c]}] [{matriz[c+1]}] [{matriz[c+2]}]')
