# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços

frase = str(input('Digite a frase: ')).lower().strip()

semEsp = frase.replace(' ','')

if semEsp == semEsp[::-1]:
    print('É um palindromo')
    print(semEsp[::-1])
else:
    print('Nao é um palindromo')
    print(semEsp[::-1])