#Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidades ele jogou. Depois vai le a quantidade de gols feito em cada partida
# no final, tudo isso será quardado em um dicionario incluindo o toral de gols feito durenta o campeonato.

dados = {}

dados['nome'] = str(input('Nome do jogador: '))
quantidade = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = []
print('=='*30)
for c in range(1,quantidade+1):
    dados['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
dados['total'] = sum(dados['gols'])
print('=='*30)
for k, v in dados.items():
    print(f'o campo {k} tem o valor de {v}')
print('=='*30)
print(f'O jogador {dados['nome']} jogou {quantidade} partidas')
for c in range(1, len(dados['gols'])+1):
    print(f'=> Na partida {c}, tem {dados["gols"][c-1]}')
print(f'Foi um total de {dados["total"]} gols')
    
    

    