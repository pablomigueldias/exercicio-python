# Escreva um progama que pergunte o salario de um funcionario e calcule o valo do seu aumento
# para salarios superiores a R$1250, calcule um aumento de 10%.
# para inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o seu salario: '))

if salario <= 1250:
    aumento = salario * 0.15
    total = salario + aumento
    print(f'Seu salario teve um aumento de 15% e ficou R${total:.2f} reais')
else:
    aumento = salario * 0.10
    total = salario + aumento
    print(f'Seu salario teve um aumento de 10% e ficou R${total:.2f} reais')