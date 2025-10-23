#faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais:
#o nome de um jogador e quantos gols ele marcou.
#o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido formado corretamente

def ficha(nome,gols):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')

nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))

if nome.strip() == '':
    nome = '<desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome,gols)
