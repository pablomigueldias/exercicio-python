#crie um programa que laia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input("Digite seu nome completo: ").strip().upper()


if "SILVA" in nome:
    print('Este nome tem Silva')
else:
    print('Este nome nao tem Silva')



