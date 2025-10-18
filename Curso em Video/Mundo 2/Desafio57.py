#faça um proghrama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Qual o seu sexo? [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Valor Invalido por favor digite novamente M/F: ')).strip().upper()[0]

if sexo == 'M':
    print('Voce é Masculino')
else:
    print('Voce é Feminino')