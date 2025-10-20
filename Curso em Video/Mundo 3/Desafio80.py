#Crie um programa onde o usuario digita cinco valores numéricos
# e cadastre-os em uma lista, ja na posição correta de inserção
#sem usar o sort().
#no final da lista, mostre a lista ordenada na tela.

numeros = []
for c in range(0,5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while True:
            if numero <= numeros[pos]:
                numeros.insert(pos,numero)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {numeros.sort()}')