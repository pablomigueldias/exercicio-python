#Crie um programa que cire uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# no final mostre a matriz na tela coma formatação correta
#mostrando no final:

#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha

matriz = []
somaPar = 0
soma_terceira_coluna = 0

for c in range(1,10):
    valor = int(input(f'Digite {c} valor : '))
    matriz.append(valor)

for c, nu in enumerate(matriz):
    if nu % 2 == 0:
        somaPar =  somaPar + nu

    if c % 3 == 2:
        soma_terceira_coluna += nu
maiorSegunda = max(matriz[3:6])


for c in range(0,len(matriz), 3):
    print(f'[{matriz[c]}] [{matriz[c+1]}] [{matriz[c+2]}]')

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma da da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor é {maiorSegunda}')