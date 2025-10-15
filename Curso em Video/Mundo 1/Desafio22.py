# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiuscula
# O nome com todas as letras miniscula
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite o nome completo: ').strip()
separado = nome.split()


print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(f'Seu primeiro nome é {separado[0]} e tem {len(separado[0])} letras')
