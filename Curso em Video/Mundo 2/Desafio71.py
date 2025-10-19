#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será 
# o valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues
#OBS: Considere que o caixa possui cedulas de R$50,R$20, R$10 e R$1

print("=" * 30)
print("CAIXA ELETRÔNICO")
print("=" * 30)

valor = int(input("Qual valor você quer sacar? R$ "))

total = valor
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total = total - cedula
        total_cedulas = total_cedulas + 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} ceulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break
        

