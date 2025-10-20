#Crie um programa que vai ler varios numeros e colocar em uma lista
#depois disso, crie duas lista extras que vao conter apenas os valores pares e os valores impares
#digitados, respectivamente.
#Ao final mostre o conteudo das tres listas geradas

lista = []
par = []
impar = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    condicao = str(input('Quer Continuar? [S/N]:  ')).strip().upper()[0]
    while condicao not in 'SN':
        print('Valor invalido')
        condicao = str(input('Quer Continuar? [S/N]:  ')).strip().upper()[0]
    if condicao == 'N':
        break

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')