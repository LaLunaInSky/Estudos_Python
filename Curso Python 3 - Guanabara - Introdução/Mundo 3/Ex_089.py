#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e 
#permita que o usuário possa mostrar as notas de cada aluno individualmente.

print(f'\n{'- Me informe nome e duas notas de vários alunos, e eu te devolvo o boletim de todos ou de cada um -':^104}\n')

boletimDosAlunos = []

while True:
    dadoDoAluno = []

    dadoDoAluno.append(input('Nome do Aluno(a): ').strip().capitalize())
    for nota in range(1, 3):
        dadoDoAluno.append(float(input(f'{nota}ª Nota: ')))

    boletimDosAlunos.append(dadoDoAluno[:])
    dadoDoAluno.clear()

    perguntaSobreContinuar = input('Quer adicionar mais um aluno(S/N)? ').strip().upper()

    if perguntaSobreContinuar in ('S', 'N'):
        if perguntaSobreContinuar == 'N':
            break
        else:
            
            print()

    else:
        print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m\n')

boletimDosAlunos.sort()
print(f'\n{'=-'*15}\n{'No.':<4} {'Nome.':<10} {'Média':>12}\n{'=-'*15}')

for posição, aluno in enumerate(boletimDosAlunos):
    print(f'{f'{posição + 1}.':<4} {aluno[0]:<10} {f"{((aluno[1] + aluno[2])/ 2):.1f}":>12}')
print('=-'*15, '\n')

while True:
    perguntaSobreMostrarDadoDeALuno = int(input('Quer mostrar as informações de qual aluno(a) (999 para fechar)? '))

    if perguntaSobreMostrarDadoDeALuno == 999:
        break

    elif perguntaSobreMostrarDadoDeALuno > len(boletimDosAlunos) or perguntaSobreMostrarDadoDeALuno < 1:
        print(f'\033[31mAPENAS É ACEITO 1 À {len(boletimDosAlunos)}\033[m\n')
        
    else:
        print(f'\n\033[34mO(a) aluno(a) {boletimDosAlunos[perguntaSobreMostrarDadoDeALuno - 1][0]} tem as notas {boletimDosAlunos[perguntaSobreMostrarDadoDeALuno - 1][1]} e {boletimDosAlunos[perguntaSobreMostrarDadoDeALuno - 1][2]}.\033[m\n')

print()