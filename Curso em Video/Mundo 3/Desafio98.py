#Faça um programa que tenha um função chamada contador(), que receba tres parametros: inicio,fim, passo
# e realiza a contagem.
#seu programa tem que realizar tres contagens atraves da função criada:
#a) de 1 até 10, de  1 em 1
#b) de 10 até 0, de  2 em 2
#c) Uma contagem personalizada

from time import sleep

def linha():
    print('=-'*20)

def contador(inicio,fim,passo):
    linha()
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio > fim:
        passo = -passo
        fim = fim - 1
    elif inicio < fim:
        passo = abs(passo)
        fim = fim + 1

    for c in range(inicio,fim,passo):
        print(f'{c}',end=' ', flush=True)
        sleep(0.4)
    print('Fim!')

contador(1,10,1)
contador(10,0,2)

linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)