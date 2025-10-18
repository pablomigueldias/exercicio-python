#crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# seu programa deverá realixar a opreção solicitada em cada caso

numero1 = int(input('Digite o primeiro numero inteiro: '))
numero2 = int(input('Digite o segundo numero inteiro: '))

condicao = 0
while condicao != 5:
    print('[1] Somar | [2] Multiplicar | [3] Maior | [4] Novos numeros | [5] Sair')
    condicao = int(input('Qual sua escolha?: '))
    if condicao == 1:
        soma = numero1 + numero2
        print(f'{numero1} + {numero2} = {soma}')
    elif condicao == 2:
       multiplicar = numero1 * numero2
       print(f'{numero1} x {numero2} = {multiplicar}') 
    elif condicao == 3:
        if numero1 > numero2:
            print(f'{numero1} é maior')
        if numero2 > numero1:
            print(f'{numero2} é maior')
    elif condicao == 4:
        numero1 = int(input('Digite o primeiro numero inteiro: '))
        numero2 = int(input('Digite o segundo numero inteiro: '))



