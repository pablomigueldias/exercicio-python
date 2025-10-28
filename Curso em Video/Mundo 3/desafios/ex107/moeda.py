

def moeda(p=0,simbolo='R$'):
    return f'{simbolo}{p:.2f}'.replace('.', ',')

def metade(p=0,formato=False):
    resultado = p / 2
    return resultado if not formato else moeda(resultado)# type: ignore


def dobro(p=0,formato=False):
    resultado = p * 2
    return resultado if not formato else moeda(resultado)


def aumentar(p=0, n=0,formato=False):
    resultado = p + (p * n / 100)
    return resultado if not formato else moeda(resultado)# type: ignore


def diminuir(p=0, n=0,formato=False):
    resultado = p - (p * n / 100)
    return resultado if not formato else moeda(resultado) # type: ignore

def resumo(valor,aum,dim):
    print(f'A metade de {moeda(valor)} é {metade(valor, True)}') # type: ignore
    print(f'O dobro de {moeda(valor)} é {dobro(valor, True)}') # type: ignore
    print(f'Aumentando {aum}%, temos {aumentar(valor, True)}') # type: ignore
    print(f'Reduzindo {dim}%, temos {diminuir(valor, True)}') # type: ignore




