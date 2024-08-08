#Faça um programa que leia o genêro de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print(f'\n{'- Me informe seu Genêro -':^30}\n')

genêro = ''

while genêro not in ['f', 'm']:
    genêro = str(input('Qual o seu genêro(F ou M)? ')).strip().lower()

    if genêro not in ['f', 'm']:
        print('\033[31mResposta INVÁLIDA! Apenas F ou M\033[m\n')

print(f'\nVocê digitou {genêro.upper()}...', end=' ')

if genêro == 'f':
    print('FEMININO\n')
else:
    print('MASCULINO\n')