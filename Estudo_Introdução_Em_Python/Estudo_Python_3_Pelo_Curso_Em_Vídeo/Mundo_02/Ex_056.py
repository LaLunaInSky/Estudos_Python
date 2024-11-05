#Desenvolva um programa que leia o nome, idade, e o genêro de 4 pessoas. No final do progrma mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.

print(f'\n{'- Me informe o nome, a idade, e o genêro de 4 pessoas, e eu te devolvo algumas informações -':^97}\n')

totalDasIdades = 0
homemMaisVelho = ''
idadeDoHomemMaisVelho = 0
mulheresAbaixoDe20Anos = 0

for contagem in range(1, 5):
    genêro = ''

    print(f'{f' {contagem}ª Pessoas ':-^31}')

    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    totalDasIdades += idade
        
    while genêro not in ['F', 'M']:
        genêro = str(input('Genêro(F/M): ')).upper().strip()

        if genêro not in ['F', 'M']:
            print('\033[31mApenas F ou M é aceito!\033[m\n')

    print()

    if genêro == 'M':
        if idadeDoHomemMaisVelho == 0:
            idadeDoHomemMaisVelho = idade
            homemMaisVelho = nome

        elif idade > idadeDoHomemMaisVelho:
            idadeDoHomemMaisVelho = idade
            homemMaisVelho = nome

    if genêro == 'F':
        if idade < 20:
            mulheresAbaixoDe20Anos += 1

if mulheresAbaixoDe20Anos == 1:
    pluralMulheres = ''
else:
    pluralMulheres = 'es'

print(f'''A média da idade de todos é {totalDasIdades / 4:.1f} anos.
O Homem mais velho foi o {homemMaisVelho} que tem {idadeDoHomemMaisVelho} anos.
No total temos {mulheresAbaixoDe20Anos} mulher{pluralMulheres} abaixo de 20 anos.
''')