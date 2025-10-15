#faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "a"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez

frase = input('Digite uma frase: ').upper().strip()
quantos = frase.count('A')
primeiro = frase.find('A') + 1
ultima = frase.rfind('A') + 1

print(frase)
print(f'Quanidades de "A" que aparece na frase: {quantos}')
print(f'Posição do primeiro "A": {primeiro}')
print(f'Posição do ultimo "A": {ultima}')
