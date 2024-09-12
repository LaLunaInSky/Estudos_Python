#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
#A)Quantidade de notas; B)A maior nota; C)A menor nota; D)A média da turma; E)A situação (opcional). 
#Adicione também as docstrings.

print(f'\n{'- Me informe quantas notas quiser, e eu te devolvo a média das mesmas e a situção caso queira -':^100}\n')

def notas(*notas, mostrarSituação=False):
    """
    -> Função que obtem várias notas informadas, devolvendo qual é a maior e a menor, a média entre todas, e caso queira a situção final.
    :parâmetro *notas: Pode-se informar quantas notas quiser.
    :parâmetro mostrarSituação: <OPCIONAL> Mostra a situação final baseada na média das notas.
    :retorna: Um dicionário com todas as informações finais. 
    """

    informaçãoDasNotas = {}
    informaçãoDasNotas['total de notas'] = len(notas)
    informaçãoDasNotas['maior nota'] = max(notas)
    informaçãoDasNotas['menor nota'] = min(notas)
    informaçãoDasNotas['média das notas'] = sum(notas) / len(notas)

    if mostrarSituação == True:
        if informaçãoDasNotas['média das notas'] < 5:
            informaçãoDasNotas['situação final'] = 'REPROVADO'
        
        elif informaçãoDasNotas['média das notas'] >= 7:
            informaçãoDasNotas['situação final'] = 'APROVADO'
        
        else:
            informaçãoDasNotas['situação final'] = 'RECUPERAÇÃO'

    return informaçãoDasNotas


informaçãoDeNotaDoAluno = notas(8, 6, 7, 10, mostrarSituação=True)

print(informaçãoDeNotaDoAluno, '\n')

help(notas)