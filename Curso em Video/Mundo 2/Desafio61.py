#refaça o Desafio51, lendo o primeiro termo e a razão de uma PA mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))

termo = a1
contador = 1
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + r
    contador += 1
print('FIM')

