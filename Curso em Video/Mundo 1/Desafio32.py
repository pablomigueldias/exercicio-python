#faça um progama que leia um ano qualquer e mostre se ele pe Bissexto

ano = int(input('Digite o ano pra eu falar se ele é BISSEXTO ou nao: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'Nao é BISSEXTO')