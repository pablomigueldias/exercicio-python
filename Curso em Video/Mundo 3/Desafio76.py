# Crie um programa que tenha um tupla unica com nomes de produtos e seu respectivos preços, na sequencia.
# no final, mostre uma listagem de preço, organizando os dados em forma tabular.

listagem = ('Lapis',
            1.75,
            'Borracha',
            2.00,
            'Caderno',
            15.90,
            'Estojo',
            25.00,
            'Transferidor',
            4.20,
            'Compasso',
            9.99,
            'Mochila',
            120.32,
            'Canetas',
            22.30,
            'Livro',
            34.90
            )

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for c in range(0, len(listagem),2):
    nome = listagem[c]
    preco = listagem[c + 1]
    
    print(f'{nome:.<30}R${preco:7.2f}')

    
