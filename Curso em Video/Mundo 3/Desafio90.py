#Faça um programa que leia o nome e média de um aluno, guardando tambem a situação em um dicionario.
#No final, mostre o conteudo da estrutura na tela.

dados = {}

dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['media'] = float(input(f'Media de {dados["nome"]}: '))


print(f'O nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
if dados['media'] >= 7:
    print('Situação Aprovado')
else:
    print('Reprovado')