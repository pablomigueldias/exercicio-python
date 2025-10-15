#Desenvolva um programa que leia o comprimento de tres restas e diga ao usuario se elas podem ou nao formar um triangulo.

retaA = float(input('tamanho da primeira reta: '))
retaB = float(input('tamanho da segunda reta: '))
retaC = float(input('tamanho da terceira reta: '))

if retaA < retaB + retaC and retaB < retaA + retaC and retaC < retaA + retaB:
    print('essas retas forma um triangulo')
else:
    print('essas retas não forma um triangulo')