#Adapte o codigo do desafio 107, criando uma função adicional
#chamada moeda que consiga mostrar os valores como um valr monetario formatado

from desafios.ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')# type: ignore
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')# type: ignore
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')# type: ignore
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}') # type: ignore