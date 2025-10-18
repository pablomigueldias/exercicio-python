#Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado
#pelo usuario. O programa será interrompido quando o numero solicitado for negativo

contador = 1
reset = 10
while True:
    numero = int(input('Qual tabuada voce quer que eu gere? '))
    if numero < 0:
        break
    if contador > 10:
        contador = contador - reset
    while contador < 11:
        multiplicacao = numero * contador
        print(f'{numero} x {contador:2} : {multiplicacao}')
        contador += 1
        
        
    

