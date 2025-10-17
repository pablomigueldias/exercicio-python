# Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. no final do programa, mostre:

# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

soma_idades = 0
homem_mais_velho = ''
idade_homem = 0
idade_mulhere = 20
qtd_mulher = 0


for c in range(1, 5):
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual seu sexo ? [F/M]: ')).upper().strip()[0]
    soma_idades = soma_idades + idade

    if sexo == 'M':
        if idade > idade_homem:
            idade_homem = idade
            homem_mais_velho = nome

    if sexo == 'F':
        if idade < idade_mulhere:
            qtd_mulher = qtd_mulher + 1


media = soma_idades / 4

print(f'A media de idade do grupo é {media:.0f} anos')
print(f'O nome do homem mais velho é {homem_mais_velho.capitalize()} e tem {idade_homem} anos')
print(f'e tem {qtd_mulher} de mulheres com menos de 20 anos')
    

