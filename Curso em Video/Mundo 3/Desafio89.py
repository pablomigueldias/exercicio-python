#Crie um programa que leia nome e duas notas de varios alunos
#e guarde tudo em uma lista compost
cadastros = []
dados = []
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    cadastros.append(dados[:])
    dados.clear()
    
    condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while condicao not in 'SN':
        condicao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if condicao == 'N':
        break
   
while True:

    for c, cadastro in enumerate(cadastros):
        media = (cadastro[1] + cadastro[2]) / 2
        print(f'{c:<5} {cadastro[0]:<20} {media:>5}')

    condicao = -1
    while condicao != 999:
        condicao = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
        if condicao == 999:
            break
        print(f'Notas de {cadastros[condicao][0]} são {cadastros[condicao][1]} {cadastros[condicao][2]}')
    if condicao == 999:
        break
