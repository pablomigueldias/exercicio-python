#faça um programa que leia um angulo qualquer e mostre na tela
# o valor de seno, conseno e tangente desse angulo.
import math
angulo = math.radians(int(input('Digite o Angulo: ')))
seno = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)

print(f'Seno: {seno:.2f}')
print(f'Cos: {cos:.2f}')
print(f'Tang: {tang:.2f}')