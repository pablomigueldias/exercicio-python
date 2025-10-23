# Crie um programa que tenha uma função factorial() que receba dois parametros: o primeiro que indique o numero a calcular
# e o outro chamadp show, que será um valor lógico (opcional) indicando se será mostrado ou nao na tela o processo de calculo do fatorial

def factorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :return: O valor do fatorial de num.
    """
    f = 1
    for c in range(num, 0, -1):
        
        f = f * c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


print(factorial(5, False))

help(factorial)
