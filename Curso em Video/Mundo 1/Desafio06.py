# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um numero inteiro: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)

print(f'Seu numero é {numero}')
print(f'O dobro é {dobro}')
print(f'O triplo é {triplo}')
print(f'A raiz quadrada é {raiz:.2f}')
