#Desenvolva umna lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela a baixo:

# - abaixo de  18.5: Abaixo do peso
# - entre 18.5 e 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Qual é o seu peso? : '))
altura = float(input('Qual é a sua Altura? : '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso')
    print(f'Seu imc é {imc:.1f}')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
    print(f'Seu imc é {imc:.1f}')
elif imc < 30:
    print('Sobrepeso')
    print(f'Seu imc é {imc:.1f}')
elif imc < 40:
    print('Obesidade')
    print(f'Seu imc é {imc:.1f}')
else:
    print('Obesidade Morbida')
    print(f'Seu imc é {imc:.1f}')