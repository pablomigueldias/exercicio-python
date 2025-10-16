# Refaça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo
# será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferente

retaA = float(input('tamanho da primeira reta: '))
retaB = float(input('tamanho da segunda reta: '))
retaC = float(input('tamanho da terceira reta: '))

if retaA < retaB + retaC and retaB < retaA + retaC and retaC < retaA + retaB:
    print('essas retas forma um triangulo')
    if retaA == retaB == retaC:
        print('é um Equilátero')
    elif retaA == retaB or retaB == retaC or retaC == retaA:
        print('é um Isósceles')
    elif retaA != retaB != retaC != retaA:
        print('é um Escaleno')
else:
    print('essas retas não forma um triangulo')