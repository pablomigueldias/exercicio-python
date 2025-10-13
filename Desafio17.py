#Faça um progama que laia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math

ca = float(input('Qual o Cateto adjacente? : '))
co = float(input('Qual o Cateto Oposto?: '))

hipotenusa = math.hypot(ca,co)

print(f'A hipotenusa é {hipotenusa:.2f}')

