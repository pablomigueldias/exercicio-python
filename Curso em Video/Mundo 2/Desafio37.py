#Escreva um programa que leia um numero inteiro qualquer e peça para o usuraio escolher qual
#sera a base de conversar:

# 1 binario
# 2 octal
# 3 hexadecimal

numero = int(input('Digite um numero inteiro: '))
print ('-='*20)
print('Para converter digite:')
print('1- Para Binario | 2- Para Octal | 3- Para Hexadecimal')
print ('-='*20)
escolha = int(input('Digite o numero : '))

if escolha == 1:
    print(f'O {numero} em binario é \033[1;35m{bin(numero)}\033[m')
elif escolha == 2:
    print(f'O {numero} em Octal é \033[1;35m{oct(numero)}\033[m')
elif escolha == 3:
    print(f'O {numero} em Hexadecimal é \033[1;35m{hex(numero)}\033[m')

