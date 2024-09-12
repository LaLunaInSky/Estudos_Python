#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final. de acordo com a média atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior: APROVADO

print(f'\n{'- Me informe duas notas do aluno, eu te devolvo a média delas, e se aluno passou, foi reprovado, ou está de recuperação -':^126}\n')

primeiraNota = float(input('Qual a 1ª Nota? '))
segundaNota = float(input('Qual a 2ª Nota? '))
médiaDoAluno = (primeiraNota + segundaNota) / 2

print(f'\nO aluno ficou com a média de {médiaDoAluno:.1f}, ele está', end=' ')

if médiaDoAluno >= 7.0:
    print('APROVADO!\n')

elif 5.0 <= médiaDoAluno <= 6.9:
    print('de RECUPERÇÃO!\n')

else:
    print('REPROVADO!\n')