#Um professor que sortear um do seus quatro alunos para apagar o quadro.
#Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido
import random

alunos = ["Pablo","Igor","Monique","Lais"]
sorteado = random.choice(alunos)

print(f'O Aluno que vai apagar o quadro é : {sorteado}')
