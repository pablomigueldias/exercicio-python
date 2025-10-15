# O mesmo professor do desafio anterior quer sortear a ordem  de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = (input('Qual o nome do 1º Aluno: '))
aluno2 = (input('Qual o nome do 2º Aluno: '))
aluno3 = (input('Qual o nome do 3º Aluno: '))
aluno4 = (input('Qual o nome do 4º Aluno: '))

alunos = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(alunos)

for i, nome in enumerate(alunos, start=1):
    print(f'{i}º {nome}')



