#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario
#ou entao o emprestimo será negado

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario? '))
anos = int(input('Quantos anos vai pagar? '))

meses = anos * 12
parcelas = casa / meses

if parcelas > salario * 0.30:
    print(f'As parcelas seria \033[1;32m{parcelas}\033[m por mes e seu salario é \033[1;32m{salario}\033[m')
    print(f'infelizmente as parceleas passa de \033[1;35m30% do seu salario\033[m')
    print('Não terá imprestimo')
elif parcelas < salario * 0.30:
    print('Emprestimo aprovado')





