#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
#indo de 10 até 0, e com uma pausa de 1 segundo entre eles

from time import sleep

print('=='*10)
print('Contagem Regressiva')
print('=='*10)

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BOOOOOM!')