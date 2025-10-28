# modifique as funções que doram criadas no desafio 107 para que eleas aceitem um parametro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108


from desafios.ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}') # type: ignore
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}') # type: ignore
print(f'Aumentando 10%, temos {moeda.aumentar(p, True)}') # type: ignore
print(f'Reduzindo 13%, temos {moeda.diminuir(p, True)}') # type: ignore
