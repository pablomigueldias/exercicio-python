# Crie um programa que leia varios numeros inteiros pelo teclado. no final fa execução, mostre a média entre todos os valores
# lidos. o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar os valores

numero = 0
contador = 0
soma = 0
condicao = 'S'
numeros = []

while condicao == 'S':
    numero = int(input('Digite um numero inteiro: '))
    numeros.append(numero)
    soma = soma + numero
    contador = contador + 1
    condicao = str(input('Quer continuar [S/N]')).upper().strip()[0]
    

media = soma / contador

print(f'A media dos numeros é {media}')
print(f'O maior numero é {max(numeros)}')
print(f'O menor numero é {min(numeros)}')


