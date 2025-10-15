# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou nao com o nome santo

nome = input('Digite o nome de uma cidade: ').upper().strip()

if "SANTO" in nome:
    print('Essa cidade tem santo')
else:
    print('Esta cidade nao tem santo')
