# Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteia() e SomaPar()
# A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função
# vai mostrar a sima entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia():
    lista = []
    for c in range(0, 5):
        numero = randint(1, 10)
        lista.append(numero)
    print(f'Sorteando 5 valores da lista : {lista}')
    return lista


def somaPar(lis):
    soma = 0
    for c in range(0, len(lis)):
        if lis[c] % 2 == 0:
            soma = soma + lis[c]
    print(f'Somando os valores pares de {numeros} temos {soma}')


numeros = sorteia()
somaPar(numeros)
