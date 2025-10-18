# Melhore o desafio 061, perguntando pra o usuraio se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostrar 0 termos

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))


contador = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while contador <= total:
        termo = a1 + (contador - 1) * r
        print(f'{termo} -> ', end='')
        contador += 1
    mais = int(input('\nQuantos a mais voce quer? '))
print('FIM')
