#faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
#retangular(largura e comprimento ) e mostre a area do terreno.


def area(a,b):
    terreno = a * b
    print(f'A área de um terreno de {a}x{b} é de {terreno}m².')

print('Controle de Terrenos')
print('-'*20)
a = float(input('LARGURA(m): '))
b = float(input('COMPRIMENTO(m): '))

area(a,b)