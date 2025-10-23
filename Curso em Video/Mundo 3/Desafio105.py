# Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes
# informações:
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a media da turma
# - a situação (opicional)
# Adicone tambem as docsstrings da função

def notas(*num, sit=False):
    """
    -> Analisa notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não incluir a situação da turma.
    :return: Um dicionário com informações sobre a turma:
             - total: quantidade de notas informadas
             - maior: a maior nota
             - menor: a menor nota
             - media: média da turma
             - situação: (opcional) avaliação da média geral
    """
    dados = {}
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = sum(num) / len(num)
    if sit:
        if dados['media'] > 7:
            dados['situação'] = 'Boa'
        elif dados['media'] < 7:
            dados['situação'] = 'Razoavel'
        elif dados['media'] < 5:
            dados['situação'] = 'Ruim'
    return dados


resp = notas(3.5, 10, 6.5)
print(resp)
help(notas)
