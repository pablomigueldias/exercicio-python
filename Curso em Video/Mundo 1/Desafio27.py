#Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input('Digite o nome completo: ').upper().strip()
separado = nome.split()

print(f'{separado}')
print(f'Primeiro nome {separado[0]}')
print(f'Ultimo nome {separado[-1]}')



