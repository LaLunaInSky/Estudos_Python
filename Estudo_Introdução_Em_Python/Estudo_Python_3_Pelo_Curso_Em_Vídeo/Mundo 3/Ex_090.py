#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

print(f'\n{'- Me informe o nome e a média de um aluno, e eu te devolvo sua situação final -':^84}\n')

informaçãoDoAluno = {}
informaçãoDoAluno['nome'] = input('Qual o nome do aluno(a)? ').strip().capitalize()
informaçãoDoAluno['média'] = float(input(f'Qual a média de {informaçãoDoAluno["nome"]}? '))

if informaçãoDoAluno['média'] >= 7:
    informaçãoDoAluno['situação'] = '\033[32mAprovado\033[m'
elif informaçãoDoAluno['média'] >= 5:
    informaçãoDoAluno['situação'] = 'de \033[33mRecuperação\033[m'
else:
    informaçãoDoAluno['situação'] = '\033[31mReprovado\033[m'

print(f'''
O(a) aluno(a) {informaçãoDoAluno["nome"]} com a média de {informaçãoDoAluno["média"]},
Está {informaçãoDoAluno["situação"]}!
''')