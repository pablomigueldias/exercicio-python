#Crie um programa que vai ler varios numeros e coloca em uma lista.
# Depois disso, mostre:
#A) Quantos numetos foram digitados.
#B) A lista de valores,ordenadas de forma decrescente.
#C) Se o valor 5 foi digitado e esta ou não na lista

lista = []
qtdnumeros = 0
while True:
    numeros = int(input('Digite um numero: '))
    qtdnumeros += 1
    lista.append(numeros)
    condicao = str(input('Quer Continuar? [S/N]:  ')).strip().upper()[0]
    while condicao not in 'SN':
        print('Valor invalido')
        condicao = str(input('Quer Continuar? [S/N]:  ')).strip().upper()[0]
    if condicao == 'N':
        break

print(f'Foram digitados {qtdnumeros} numeros')
print(f'Lista de forma decrescente: {sorted(lista,reverse=True)}')
if 5 in lista:
    print(f'Tem 5 na lista')
else:
    print(f'nao tem 5 na lista')