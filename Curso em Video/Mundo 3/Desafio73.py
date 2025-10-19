#Crie um tupla preenchida com os 20 primeiros colocados da tabela do Compeonato Brasileiro de Futebook,
#na ordem de colocação. depois mostre:

#A) Apenas os 5 primeiros colocados
#B) os ultimos 4 colocados da tabela
#C) Uma losta com os times em ordem alfabética.
#D) em que posição na tabela está o time da Chapecoense

times = (
    "Palmeiras",
    "Flamengo",
    "Internacional",
    "Grêmio",
    "São Paulo",
    "Atlético Mineiro",
    "Athletico Paranaense",
    "Cruzeiro",
    "Botafogo",
    "Santos",
    "Bahia",
    "Corinthians",
    "Fluminense",
    "Ceará",
    "Vasco da Gama",
    "Chapecoense",
    "Vitória",
    "América Mineiro",
    "Paraná",
    "Sport"
)
print(f'Lista do times do Brasileirão: {times} ')
print(f'Os 5 primeiros são : {times[0:5]}')
print(f'Os 4 ultimos são : {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª Posição')