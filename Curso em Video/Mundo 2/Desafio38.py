# Escreva um progama que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# nao existe valo maior, os dois são iguais

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 > numero2:
    print(f'O {numero1} é maior {numero2}')
elif numero2 > numero1:
    print(f'O {numero2} é maior que o {numero1}')
elif numero1 == numero2:
    print(f'O {numero1} e {numero2} são numeros iguais')
