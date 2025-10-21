#Aprimore o Desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.


dados = {}
jogadores = []
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    quantidade = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = []
    print('=='*30)
    for c in range(0,quantidade):
        dados['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())
    print('=='*30)
    condicao = str(input('Quer Continuar? [S/N]: ')).upper().strip()
    while condicao not in 'SN':
        print('Valor invalido, tente novamente...')
        condicao = str(input('Quer Continuar? [S/N]: ')).upper().strip()
    if condicao == 'N':
        break

print(f'{"Cod":<5}{"Nome":^20}{"Gols":^20}{"Total":>10}')
print('-' * 55)

for c in range(len(jogadores)):
    print(f'{c:<5}{jogadores[c]["nome"]:^20}{str(jogadores[c]["gols"]):^20}{jogadores[c]["total"]:>10}')

mostrar = int(input('Mostrar dados de qual jogador? '))
print(F'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}')
for c in range(0,len(jogadores[mostrar]['gols'])):
    print(f'No jogo {c} fez {jogadores[mostrar]['gols'][c]} gols.')

while True: 
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break
    print(F'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]['nome']}')
    for c in range(0,len(jogadores[mostrar]['gols'])):
        print(f'No jogo {c} fez {jogadores[mostrar]['gols'][c]} gols.')
    





    
        
 
    
 
