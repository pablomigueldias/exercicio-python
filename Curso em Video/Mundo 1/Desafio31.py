#Desenvolva um progama que pergunte a distancia de uma viagem em Km.
#calcule o preço da passagem, cobrando R$0,50 por km para viagem de até 200km
# R$ 0,45 para viagens mais longas

distancia = int(input('Qual é a distancia da viagem? '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Sua viagem de {distancia}Km/h tera um custo de R${valor:.2f} reais')
else:
    valor = distancia * 0.45
    print(f'Sua viagem de {distancia}Km/h tera um custo de R${valor:.2f} reais')