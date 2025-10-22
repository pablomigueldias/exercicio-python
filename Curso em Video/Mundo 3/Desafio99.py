#Faça um programa que tenha um função chamada maior(), que receba varios parametros com valores inteiros.
#seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def linhas():
    print('=-'*20)

def maior(*numeros):
    linhas()
    print('Analisando os valores passados...')
    if numeros == 0:
        print(f'Foram informados {len(numeros)} valores ao todo')
        print(f'O maior valor informado foi {max(numeros)}')
    else:
        for c in range(0, len(numeros)):
            print(f'{numeros[c]}', end=' ', flush=True)
            sleep(0.4)
        print(f'Foram informados {len(numeros)} valores ao todo')
        print(f'O maior valor informado foi {max(numeros)}')




maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
