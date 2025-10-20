#Crie um programa onde o usuario digite uma expressão qualquer
# que use parenteses. seu aplicativo deverá analisar se a expressão
#passa esta com os parenteses avertos e fechados na ordem correta

expressão = input('Digite uma expressão: ')

pilha = []

for simbolo in expressão:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')