#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os em 
# um dicionario se por acaso o CTPS for diferente de zero, o dicionario receberá tambem
#o ano de contratração e o salario. Calcule e Acrscente, alem da idade, com quantos anos 
# a pessoa vai se aposentar.
import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.datetime.now().year - dados['nascimento']
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))


if dados['CTPS'] != 0:
   
   dados['contratacao'] = int(input('Ano de contratação: '))
   dados['salario'] = float(input('Salario: R$ '))
   dados['aposentadoria'] = (dados['contratacao'] - dados['nascimento']) + 35
   

print(dados)

for key,valor in dados.items():
   print(f'{key} tem o valor {valor}')

