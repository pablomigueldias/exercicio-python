#Escreva um programa que leia a velocidade de um carro

#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite 

velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    sobrou = velocidade - 80
    multa = sobrou * 7
    print(f'Você passou de 80km/h recebeu uma multa de R${multa:.2f} Reais') 
else:
    print(f'Você esta na velocidade permitida')