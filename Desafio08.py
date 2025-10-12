# Escreva um programa que laia um valor em metros e o exiba convertido em centimetros e milimetros

numero = int(input('Digite o numero em metros: '))
centimetro = numero * 100
milimetros = numero * 1000

print(f'{numero} metros em centimetros é {centimetro}cm')
print(f'{numero} metros em milimetros é {milimetros}mm')
