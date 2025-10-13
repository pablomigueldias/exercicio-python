#Escreva um progama que pergunte a quantidade de KM percoridos por um carro alugado e a quantidade de dias pelos quais ele foi aligado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e $0,15 por Km rodado

km = float(input('Quantos KM percorrido? : '))
dias = int(input('Quantos dias alugado? : '))
valorDias = 60 * dias
KmRodado = 0.15 * km
total = valorDias + KmRodado

print(f'Total a pagar no carro alugado é R${total:.2f}')
 