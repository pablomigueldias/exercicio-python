#Crie um programa onde o usuario poossa digitar varuos valores numerios e cadastre-os em uma lista
#Caso o numero ja exista la dentro, ele não sera adicionado. No final, serão exibidos todos os valores
#unicos digitados em ordem crescente

numeros = []

while True:
    numero = int(input('Digite um valor: '))
    
    if numero in numeros:
        print('Valor repetido nao vou adicionar')
    else:
        numeros.append(numero)
        print('Valor adicionado com suceso...')

    condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while condicao not in "SN":
        print('Condição invalida. Tente Novamente')
        condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if condicao == 'N':
        break
       

print(f'Voce digitou os valores {sorted(numeros)}')