#Faça um programa que leia a largura e a altura de uma parede em metros e 
# calcule a sua area e a quantidade de tinta necessaria para pintá-lo, 
# sabendo que cada litro de tinta pinta uma arra de 2m²

altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura * largura
litroTinta = 2
quantidade = area / litroTinta

print(f'Precisa de {quantidade} litros de tinta para pintar a parede')
