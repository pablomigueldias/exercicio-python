#Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem
#com tamanho adaptavel.

#ex: escreva('Olá,Mundo!')
# saida:
'''
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
'''

def escreva(texto):
    tamanho = len(texto) + 4
    print('~'*tamanho)
    print(f'{texto:^{tamanho}}')
    print('~'*tamanho)

escreva('Pablo Miguel')
escreva('Aprendendo Python') 
escreva('Analista de Sistemas')
    