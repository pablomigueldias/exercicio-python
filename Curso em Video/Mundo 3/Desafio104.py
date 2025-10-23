#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a funçãon input() do python
#só que fazendo a validação para aceitar apenas um valor numerico.

def leiaInt(msg):
    valor = input(msg)
    while True:
        if valor.isnumeric():
            print(f'Voce acabou de digitar o numero {int(valor)}')
            break
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            valor = input('Digita um numero inteiro: ')
            if valor.isnumeric():
                print(f'Voce acabou de digitar o numero {int(valor)}')
                break

leiaInt('Digite um valor: ')
