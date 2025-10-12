#Faça um algoritumo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input(f'Qual é o salario do funcionario? R$ '))
aumento = salario * 0.15
total = salario + aumento

print(f'O Salario do funcionario teve 15% de aumento e ficou R${total} reais')
