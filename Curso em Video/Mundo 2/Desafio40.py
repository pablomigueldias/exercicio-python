#Crie um programa que lai duas notas de um aluno e calcule sua média, mostrando uma mensagem 
#no final, de acordo com a média atingida:

# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7 ou superior: Aprovado

nota1 = float(input('Primeira Nota do aluno: '))
nota2 = float(input('Segunda Nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média é {media} ele esta abaixo de 5.')
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua média é {media} esta entre 5 e 6.9.')
    print('RECUPERAÇÃO')
elif media >= 7:
    print(f'Sua média é {media} esta nota 7 ou superior')
    print('APROVADO')
