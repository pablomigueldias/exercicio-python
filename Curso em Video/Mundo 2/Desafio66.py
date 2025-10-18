# Crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuário
#digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitador
#e qual foi a soma entre eles

soma = 0
contador = 0
while True:
    numero = int(input('Digite um numero inteiro [999 para parar]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
    
print(f'Foi digitador {contador} numeros e a soma foi {soma}')